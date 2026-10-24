
class Solution(object):
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
        """
        :type arriveAlice: str
        :type leaveAlice: str
        :type arriveBob: str
        :type leaveBob: str
        :rtype: int
        """
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def getDay(date):
            month, day = map(int, date.split('-'))
            return sum(months[:month - 1]) + day

        alice_start = getDay(arriveAlice)
        alice_end = getDay(leaveAlice)
        bob_start = getDay(arriveBob)
        bob_end = getDay(leaveBob)

        start = max(alice_start, bob_start)
        end = min(alice_end, bob_end)

        return max(0, end - start + 1)
