class Reindeer:
    def __init__(self, name, speed, speed_duration, rest_duration):
        self.name = name
        self.speed = speed
        self.speed_duration = speed_duration
        self.sprint_distance = speed * speed_duration
        self.rest_duration = rest_duration

        self.distance_travelled = 0
        self.been_resting_for_seconds = 0

        self.been_flying_for_seconds = 0
        self.time_left_resting = 0
        self.start_next_run = True
        self.skip = True

    def __str__(self):
        return "Name : " + self.name + "\tSpeed : " + str(self.speed) \
               + "\tSpeed Duration : " + str(self.speed_duration) + "\tSprint Distance : " + str(self.sprint_distance) \
               + "\tRest Duration : " + str(self.rest_duration)

    def final_stats(self):
        print self.name, "Travelled : " + str(self.distance_travelled)

    def travel(self):
        if self.time_left_resting != 0:
            self.time_left_resting -= 1
            self.been_resting_for_seconds += 1
            if self.time_left_resting == 0:
                self.start_next_run = True
                self.skip = True
        elif not self.skip and (
                self.distance_travelled >= self.sprint_distance and self.distance_travelled % self.sprint_distance == 0):
            self.time_left_resting = self.rest_duration
            self.time_left_resting -= 1  # for this round we rest
            self.been_resting_for_seconds += 1
            self.start_next_run = False
        elif self.start_next_run:
            self.skip = False
            self.distance_travelled += self.speed
            self.been_flying_for_seconds += 1
