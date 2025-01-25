class MeetingRoom:

    def check_conflict(self, meetings) -> bool:
        # first we sort

        # acutally first we are sorting via start time that is meeting[0] time
        meetings.sort( key = lambda x: x[0])

        # we check and care if start time does not overlap with end time
        for i in range(len(meetings) - 1):
            if(meetings[i][1] > meetings[i+1][0]):
                return False
            
            return True
        
meeting_room = MeetingRoom()

print(meeting_room.check_conflict([[0, 1], [2, 4], [1, 3], [5, 6]]))
print(meeting_room.check_conflict([[7, 10], [2, 4], [1, 3], [5, 6]]))