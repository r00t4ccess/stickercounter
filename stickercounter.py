#!/usr/bin/env python

def compareString(word, compare):
    # Need at least 1 sticker
    stickerCount = 1
    # iterate through the first word to find
    # the mode letter of the second word
    for letter in word:
        numOccur = compare.count(letter)
        if numOccur > 1:
            # see how many stickers a particular char would require by dividing
            # the char count of letter from the second word based on its occurance
            # in the first word
            difference = abs(compare.count(letter) / word.count(letter))
            remainder = abs(compare.count(letter) % word.count(letter))
            # Cannot have a partial sticker so a remainder requires another full sticker
            if remainder > 0:
                remainder = 1
            else: 
                remainder = 0
            
            # if the amount of stickers required by this letter are greater than 
            # that of the current then that is the new required amount
            if stickerCount < difference:
                stickerCount = difference + remainder

    return int(stickerCount)


baseWord = input("Enter base word: ")
compareWord = input("Enter compare word: ")

numStickers = compareString(baseWord, compareWord)

print("Number of stickers needed: " + str(numStickers))