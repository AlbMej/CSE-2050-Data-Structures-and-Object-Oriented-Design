from logentry import LogEntry
from Mappings import HashMapping
from lastk import LastK
import unittest

class BadLoginDetector:
    def __init__(self,k,s):
        self.threshold = k
        self.time_limit = s
        self.data = HashMapping() 
        self.failures = set()
        self.last_fail = None

    def process(self,logentry):
        time_now = logentry.time
        ipa = logentry.ip
        if ipa not in self.data: self.data[ipa] = LastK(self.threshold)

        if logentry.success == 'SUCCESS':
            self.last_fail = None
            self.data[ipa].clear()

        elif logentry.success == 'FAIL':
            if self.last_fail is None: self.last_fail = time_now
            failures = self.data[ipa]
            failures.add(logentry)
            self.data[ipa] = failures

            #print([i.time for i in failures.data],'Time now:',time_now, 'First Fail:',failures[0].time, "Limit:",self.time_limit, "*******", (time_now-failures[0].time) < self.time_limit)
            if len(self.data[ipa]) == self.threshold and (time_now-failures[0].time) < self.time_limit:
                #print([i.time for i in failures.data], time_now, failures[0].time, self.time_limit, "*******")
                if ipa not in self.failures: self.failures.add(logentry.ip)
                return False
            self.last_fail = time_now
        return True

    def report(self):
    	return list(self.failures)

    def log_details(self, newentry):
        print("---------------------------")
        print('New entry:',newentry)
        print('Failures:',self.failures)
        print('Data:',self.data)
        for key,value in self.data.items():
            print('Key: {}'.format(key), 'Value:', [log.time for log in value.data])
        print("---------------------------")

