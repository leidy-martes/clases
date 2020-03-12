class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num.replace(" ", "")

    def valid(self):
        card_num = ""
        for num in self.card_num:
            if num.isdigit():
                card_num += num
            else:
                return False
        if len(card_num) <= 1:
            return False
        nums = []
        for num in card_num:
            nums.append(int(num))
        nums.reverse()
        for i in range(len(nums)):
            if i % 2 != 0:
                nums[i] *= 2
        for i in range(len(nums)):
            if nums[i] > 9:
                nums[i] -= 9
        if sum(nums) % 10 == 0:
            return True
        else:
            return False
    