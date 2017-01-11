import time

class Timer:
    def start(self):
        self.starttime = time.localtime()

    def stop(self):
        time.sleep(5)
        self.stoptime = time.localtime()
        self._duration()
        print self.prompt

    def _duration(self):
        self.durationtime = []
        self.prompt = "running"
        for i in range(6):
            self.durationtime.append(self.stoptime[i] - self.starttime[i])
            self.prompt += str(self.durationtime[i])


a = Timer()
a.start()
a.stop()
