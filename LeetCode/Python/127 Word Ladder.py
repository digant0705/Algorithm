# -*- coding: utf-8 -*-

'''
Word Ladder
===========

Given two words (beginWord and endWord), and a dictionary's word list, find the
length of shortest transformation sequence from beginWord to endWord, such
that:

- Only one letter can be changed at a time
- Each intermediate word must exist in the word list

For example,

Given:

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",

return its length 5.

Note:
- Return 0 if there is no such transformation sequence.
- All words have the same length.
- All words contain only lowercase alphabetic characters.
'''


import collections


class Solution(object):
    '''算法思路：

    BFS 搜寻，效率差主要是查找关联顶点这一块

    结果：TLE
    '''
    def cache(f):
        def method(obj, a, b):
            if a > b:
                a, b = b, a
            key = '{}:{}'.format(a, b)
            if key not in obj.cache:
                obj.cache[key] = f(obj, a, b)
            return obj.cache[key]
        return method

    @cache
    def connected(self, a, b):
        count = 0
        for i in xrange(len(a)):
            count += a[i] != b[i]
            if count > 1:
                return False
        return count == 1

    def ladderLength(self, beginWord, endWord, wordList):
        self.cache = {}
        path = collections.defaultdict(set)

        queue, T, distance = [beginWord], wordList, 1
        while queue:
            distance += 1
            for _ in xrange(len(queue)):
                peek = queue.pop(0)

                for t in T:
                    if self.connected(peek, t):
                        if t == endWord:
                            return distance
                        queue.append(t)
                T.discard(peek)
        return 0


import collections
import string


class Solution(object):
    '''算法思路：

    同上，不过在查找关联顶点时用了不同的算法，假设每个单词长度为 length，wordlist
    长度为 n，则上面查找时效率为 O(length * n)，这种算法没有利用第 2，3 种条件，而
    这里利用了上述条件，效率为 O(length * 26)

    结果：AC
    '''
    def ladderLength(self, beginWord, endWord, wordList):
        queue, distance = collections.deque([beginWord]), 1
        while queue:
            distance += 1

            for _ in xrange(len(queue)):
                word = queue.popleft()
                for i in xrange(len(word)):
                    for char in string.ascii_lowercase:
                        candidate = word[:i] + char + word[i + 1:]

                        if candidate == endWord:
                            return distance

                        if candidate in wordList:
                            queue.append(candidate)
                            wordList.discard(candidate)
        return 0


class Solution(object):
    '''算法思路：

    同上，不过改成了 Two-end BFS（双端BFS）
    '''
    def ladderLength(self, beginWord, endWord, wordList):
        forward, backward, n, r = {beginWord}, {endWord}, len(beginWord), 2
        while forward and backward:
            if len(forward) > len(backward):
                forward, backward = backward, forward

            next = set()
            for word in forward:
                for i, char in enumerate(word):
                    first, second = word[:i], word[i + 1:]
                    for item in string.ascii_lowercase:
                        candidate = first + item + second
                        if candidate in backward:
                            return r

                        if candidate in wordList:
                            wordList.discard(candidate)
                            next.add(candidate)
            forward = next
            r += 1
        return 0


s = Solution()
print s.ladderLength("cet", "ism", {"kid","tag","pup","ail","tun","woo","erg","luz","brr","gay","sip","kay","per","val","mes","ohs","now","boa","cet","pal","bar","die","war","hay","eco","pub","lob","rue","fry","lit","rex","jan","cot","bid","ali","pay","col","gum","ger","row","won","dan","rum","fad","tut","sag","yip","sui","ark","has","zip","fez","own","ump","dis","ads","max","jaw","out","btu","ana","gap","cry","led","abe","box","ore","pig","fie","toy","fat","cal","lie","noh","sew","ono","tam","flu","mgm","ply","awe","pry","tit","tie","yet","too","tax","jim","san","pan","map","ski","ova","wed","non","wac","nut","why","bye","lye","oct","old","fin","feb","chi","sap","owl","log","tod","dot","bow","fob","for","joe","ivy","fan","age","fax","hip","jib","mel","hus","sob","ifs","tab","ara","dab","jag","jar","arm","lot","tom","sax","tex","yum","pei","wen","wry","ire","irk","far","mew","wit","doe","gas","rte","ian","pot","ask","wag","hag","amy","nag","ron","soy","gin","don","tug","fay","vic","boo","nam","ave","buy","sop","but","orb","fen","paw","his","sub","bob","yea","oft","inn","rod","yam","pew","web","hod","hun","gyp","wei","wis","rob","gad","pie","mon","dog","bib","rub","ere","dig","era","cat","fox","bee","mod","day","apr","vie","nev","jam","pam","new","aye","ani","and","ibm","yap","can","pyx","tar","kin","fog","hum","pip","cup","dye","lyx","jog","nun","par","wan","fey","bus","oak","bad","ats","set","qom","vat","eat","pus","rev","axe","ion","six","ila","lao","mom","mas","pro","few","opt","poe","art","ash","oar","cap","lop","may","shy","rid","bat","sum","rim","fee","bmw","sky","maj","hue","thy","ava","rap","den","fla","auk","cox","ibo","hey","saw","vim","sec","ltd","you","its","tat","dew","eva","tog","ram","let","see","zit","maw","nix","ate","gig","rep","owe","ind","hog","eve","sam","zoo","any","dow","cod","bed","vet","ham","sis","hex","via","fir","nod","mao","aug","mum","hoe","bah","hal","keg","hew","zed","tow","gog","ass","dem","who","bet","gos","son","ear","spy","kit","boy","due","sen","oaf","mix","hep","fur","ada","bin","nil","mia","ewe","hit","fix","sad","rib","eye","hop","haw","wax","mid","tad","ken","wad","rye","pap","bog","gut","ito","woe","our","ado","sin","mad","ray","hon","roy","dip","hen","iva","lug","asp","hui","yak","bay","poi","yep","bun","try","lad","elm","nat","wyo","gym","dug","toe","dee","wig","sly","rip","geo","cog","pas","zen","odd","nan","lay","pod","fit","hem","joy","bum","rio","yon","dec","leg","put","sue","dim","pet","yaw","nub","bit","bur","sid","sun","oil","red","doc","moe","caw","eel","dix","cub","end","gem","off","yew","hug","pop","tub","sgt","lid","pun","ton","sol","din","yup","jab","pea","bug","gag","mil","jig","hub","low","did","tin","get","gte","sox","lei","mig","fig","lon","use","ban","flo","nov","jut","bag","mir","sty","lap","two","ins","con","ant","net","tux","ode","stu","mug","cad","nap","gun","fop","tot","sow","sal","sic","ted","wot","del","imp","cob","way","ann","tan","mci","job","wet","ism","err","him","all","pad","hah","hie","aim","ike","jed","ego","mac","baa","min","com","ill","was","cab","ago","ina","big","ilk","gal","tap","duh","ola","ran","lab","top","gob","hot","ora","tia","kip","han","met","hut","she","sac","fed","goo","tee","ell","not","act","gil","rut","ala","ape","rig","cid","god","duo","lin","aid","gel","awl","lag","elf","liz","ref","aha","fib","oho","tho","her","nor","ace","adz","fun","ned","coo","win","tao","coy","van","man","pit","guy","foe","hid","mai","sup","jay","hob","mow","jot","are","pol","arc","lax","aft","alb","len","air","pug","pox","vow","got","meg","zoe","amp","ale","bud","gee","pin","dun","pat","ten","mob"})
