#   https://leetcode.com/problems/word-search


from copy import deepcopy
from typing import List


class Solution(object):
    #   98.02%
    def exist0(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def consume(r, c, s):
            if visited[r][c] == 1 or board[r][c] != s[0]:
                return False
            visited[r][c] = 1
            #print('visited[{}][{}] = {}\tboard[{}][{}] = {} from {}'.format(r, c, visited[r][c], r, c, board[r][c], s))
            #print('board = {}\tboard[{}][{}] = {} from {}'.format(board, r, c, board[r][c], s))
            if 1 == len(s):
                return True
            if 0 < r:
                result = consume(r - 1, c, s[1:])
                if result:
                    return result
            if 0 < c:
                result = consume(r, c - 1, s[1:])
                if result:
                    return result
            if r < MAX_ROW - 1:
                result = consume(r + 1, c, s[1:])
                if result:
                    return result
            if c < MAX_COL - 1:
                result = consume(r, c + 1, s[1:])
                if result:
                    return result
            visited[r][c] = 0
            return False

        if board is None or 0 == len(board) or 0 == len(board[0]):
            return False

        MAX_ROW = len(board)
        MAX_COL = len(board[0])
        visited = [[0] * MAX_COL for i in range(MAX_ROW)]
        for r in range(MAX_ROW):
            for c in range(MAX_COL):
                #visited = [[0] * MAX_COL for i in range(MAX_ROW)]
                if word[0] == board[r][c]:
                    result = consume(r, c, word)
                    if result:
                        return result
        return False

    #   runtime; 360ms, 68.70%
    #   memory; 14.6MB, 31.91%
    def exist1(self, board, word):

        R, C = len(board), len(board[0])

        def isValid(r, c, visited):
            if r < 0 or R <= r or c < 0 or C <= c or (r, c) in visited:
                return False
            return True

        def isIncluded(w, visited, r, c):
            visited.add((r, c))
            if 0 == len(w):
                return True
            for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if isValid(nr, nc, visited) and w[0] == board[nr][nc]:
                    if isIncluded(w[1:], visited, nr, nc):
                        return True
                    visited.remove((nr, nc))
            return False

        for r in range(R):
            for c in range(C):
                if word[0] == board[r][c]:
                    if isIncluded(word[1:], set(), r, c):
                        return True
        return False

    #   위의 code에서 visited만 set 대신 2d list 사용
    #   runtime; 348ms, 74.81%
    #   memory; 14.5MB, 31.91%
    def exist2(self, board, word):

        R, C = len(board), len(board[0])
        visited = [[False] * C for _ in range(R)]

        def isValid(r, c):
            if r < 0 or R <= r or c < 0 or C <= c or visited[r][c]:
                return False
            return True

        def isIncluded(w, r, c):
            visited[r][c] = True
            if 0 == len(w):
                return True
            for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if isValid(nr, nc) and w[0] == board[nr][nc]:
                    if isIncluded(w[1:], nr, nc):
                        return True
            visited[r][c] = False
            return False

        for r in range(R):
            for c in range(C):
                if word[0] == board[r][c]:
                    if isIncluded(word[1:], r, c):
                        return True
        return False

    #   https://leetcode.com/explore/featured/card/july-leetcoding-challenge/546/week-3-july-15th-july-21st/3397
    #   runtime; 460ms, 33.79%
    #   memory; 15.5MB, 16.28%
    def exist(self, board: List[List[str]], word: str) -> bool:
        R, C = len(board), len(board[0])

        def getChar(w, r, c):
            if board[r][c] == w[0]:
                if len(w) == 1:
                    return True
                board[r][c] = ''
                for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                    if 0 <= nr < R and 0 <= nc < C:
                        if getChar(w[1:], nr, nc):
                            return True
                board[r][c] = w[0]
            return False

        for r in range(R):
            for c in range(C):
                if board[r][c] == word[0]:
                    if getChar(word, r, c):
                        return True
        return False


board0 = [['A','B','C','E'],
          ['S','F','C','S'],
          ['A','D','E','E']
          ]
board1 = [['A', 'B', 'C', 'E'],
          ['S', 'F', 'E', 'S'],
          ['A', 'D', 'E', 'E']
          ]
board2 = [["a","a","a","a"],
          ["a","a","a","a"],
          ["a","a","a","a"],
          ["a","a","a","a"],
          ["a","a","a","b"],
          ]
board3 = [["C","A","A"],
          ["A","A","A"],
          ["B","C","D"]
          ]
data = [(deepcopy(board0), "ABCCED", True),
        (deepcopy(board0), "SEE", True),
        (board0, "ABCB", False),
        (board1, "ABCESEEEFS", True),
        (board2, "aaaaaaaaaaaaaaaaaaaa", False),
        (board3, "AAB", True),
        ([['a']], 'a', True),
        ]
s = Solution()
for board, word, expected in data:
    for b in board:
        print(b)
    real = s.exist(board, word)
    print(f'{word}, expected {expected}, real {real}, result {expected == real}')


'''
["dgtjaljwlwsbdpqnjnlvrafrtmdrecekkxvliejwcdxfsosedfbxhgoastuzxylivgtgke",
"enibsarngxuhucpkckeyjbwwjucecojgdtjwtdlaafjwjzgojkmuojqzfughirnmkykfbx",
"hberxoqgcbsoxgznigjoprfefpdrweoegvvfjnlnqednmdcullkbepfkgidfnujvpgcyvo",
"lluoaitcffnpirhpdpyhunddkslmqgcdtytthpxmwkbeeitjatsuivasnlffujkpielpvi",
"drvexzpsirmbluwnpmburvfcmngxebghuborcfjkwvnjsmxhyydptirhyzfccnkwqansfz",
"edwsmqejxchcrcnlklkpppeblubbmicqlykypohosprmrgxbtjsiywkmslneupxfphfeyn",
"vqcocvuzznjtvjshvktkrpzowrvcvtrqktgoqaorpzllkdsgpnqgesubjsfglwzxrfojgc",
"bvdminrdvgqmnxejypbfvpduouacdieedjsozjrushghgmqgbslxhorvktyobeufontnym",
"hsvqzccqieiudrkwmvqmlrrfwhurwvdfnzxnbafjgnflgqhulxhwpadnjaffvkmklkxmme",
"yurdfzvmuimbgbdkomkvtfgfrrrpgftgznjgmhviphjwiogyasutzcbqvshdydjzsvggcb",
"priapspxqppmlqomhmgqpgtzgnuouwrjpblhtaelswydmmpvyxooehpmvjcrhtcyunfpom",
"agiylwncsnzgddpsrmbtdkmfjivqxjcarkycjlgdbflelcxcpayulkcwvxouirubdtfmgl",
"rhqcmdflgwleqyquuntjibccefxjuewlnnobqvmyraejyxevkxesbivfpurjanxocnrvie",
"vzeaiexozhofcpnxwdtpoudlkhabeihajlauszkrgyxinkhmpbbgxgrhouisequodukvvu",
"nctmmiywuozwuwendujlnodjejeoezktddfsmgoiwngqllfofrbuffejokzuljqppvjddz",
"lzmsrzdznkqqfvxjglvfigqyxfvgizfuytosstrhdhyicvtkjoptxfrulodvpipqefiyyz",
"icggmkdguowjhtqaodrtzgdqyhwgiwfqynylzbttqrezlxcbatuzbxsahogpkofldfydgt",
"wykdavacyavucysuybkfqwvxhyehdkacllflifphhmbjkvfjyrqqonpxntfrgftrqaezfv",
"iohlarjfchxsynfnktjpmpvhgnhmoohycokchvkkcjecwksgfbwtstaaihmxvvxzljcseo",
"ejxjntvfzcixvasxcbeoablxawhepnsvwpekkbrmdcjaeexhfdxhejehfnnwbgszxyjkad",
"wdfhelldsshqznbgugtkfusxupxfbxkxdphhdskvltnmhosdxmncifbexymywwyzmfirzu",
"mkocxvsrypdorotusqteprbpspuagtwugkwfhpwigcwaqpuigppxgsoahicpdzjjjiqtzp",
"bfrxhjoctwtitcahcjrfavekgpuzivolahkkqzmjvfurjuamgsrgpxsxmoyxjokmvvwluk",
"xrpriznlnvfecwdwvpluouizggwcrqmqjejsfxduukywgdvbsgvjagkjmgnfycwhifbneg",
"hzqhxwksyeavpdbzmnfbtfdrnlyoafvhenqdkcykjyfybjypwfrrlukaijqiqlswbizlnx",
"vwycublurkcidpeqrmbhxrvpnwzohmoeimifnwbgifqnwvdnjexgxsxkoxzxjndubnbqje",
"xtmnhikkywrveoncbdzcakrfesshieofxaveihridkdiasmbxldzvwecozlxdzeazbhkjy",
"umiywksimqvrptowxevidykiyjlfvufqjpqhakqoanfsgvodalodjynjjbrhvyxgopoozg",
"ectluchkhjvvogvephfioahnjvexlddpfwabajnisifhqblgkqoasvnbstadwduecvhcgv",
"mzfsiwtvednsfhqslillojpiptfxxosknxcxvxszchuhokbzuolixctpxamuoegddkabhu",
"albussgvrbjeljieyfhkcvqkzvvbwewzqztktagldrroaatahamjxeuyapaytyzlztwtvc",
"gytxowxhwfjjqjpkhrbhqxhpihkeahighefwaffykrjcazpjqqtipayajkgluprdvzzveh",
"tqadsachlsaebrfbrqnycjptnksohyvaovfhxhqjcqpfiuiblxzphqiwadkjdiksfpzdzp",
"odidksautnrvcalmworhxvpjnubozcfphntrfvlbkewmfhabxsixpzgcuhsvlxlsngjsbw",
"tnbrzibbjytuvkteoplglzeyrredlhzhucyvkbwwaqqxcjbrbpxmodkfwqiixkrrormbti",
"xtansdyuwzltnbxzgtprdmdwfroruhcrcegwjfsfgdbweyvntlgzxjvfclwxuaqyhxvqen",
"ymtzixzemurstqdrvieuhzuxxduuwaiunbvvawbpqshmlnfgxjaekxbiaycyamunpplsno",
"hejqsufzackdgvakfckjbkwvannlfcboikfaekbhpmkvhkhmorvretpejerogsdpdkphwt",
"qlfajmmqabkxuorjscnjqubvjghaqetgrahamvtoydmtrfclhswzmzxxgezwktecvleijx",
"whckavpdiyveyjevimbhkmcoqycwgluesyrvwiyehvjfgpcobdvlrybhydegqakjadewme",
"btbmajbcxehurzusgsymyomlznoflclmvmyxxbzufjrwinrqgpdgfrtfgkksmwekkfhigj",
"emsxkcldstsvbapvfvhrnvpufcbpmhyqvsqiudlmwgkzgbwnwdemzwigyjxmsxeopuwlxj",
"avpmvxnrkjxrxynfgnoezhbdxtavexeevwqstdlepixmimupzitarwfqphluhsacorujwf",
"nnqkaywupxeizyhhowocqxurzikvtibhwttyrsuhrartyycpvsrnqlgpvsnodoxzhtzanv",
"jgxbbwbdnyweomrudmpqcsgctpvsskpbqmeskgxxgtduhurnigdlymnrbkltuaxmobgbje",
"aqzemhadujjzwhljapvlkrnhdejmfuqfkrjzakcwvmwrvjcwaxjloxutbdfiaxnmpzlpjo",
"oeckvxvxvwwhjkedfhjlpjkcvzbhrmvfszrpymoukkbtwhxcqgpfrzjmbnvsbszurslqea",
"mrmnmjwjnmrctkdexerswtlxpepauwagnnvbytnlheparsfoxyivtvviaklwinfxcczawm",
"ndseejxlzwjktdfonhzygjmlhongrjsepmjvwigxerhxwnokwpkcywnfndleofkdutyqdg",
"nhavhwkxiimtlkraqeddkslvxfowxuembejkdthnetgpgaryexdrpomovcmswrfaxomaku",
"oopwfvwyvdvzumniblkndhgkjebvglpwbhvietiawezssoavznlfwrpfvqaedsagbxqfrz",
"hnfiizzkvyzgfvxvavndbtxdzybsfstnhavrzucuvbcazcxbzlgagddhbezhyuwgutzuob",
"qlftngxlhwyowetblvineghaoctoyjrowyjkegvoeveabxcoukdyslahpwxnfodeppotxl",
"jcgncjngxhsbinokudgtsohxuyoismtdobtsmibjrtmzgamcfuvzkfzednmxzhdpkwiwej",
"iveuxnxlrefnequfwzsjzuscjfatbeelbliayflpjrepjaufanqzjjdsodorjsdkdlldsw",
"vbpbtacniecyfljiezlurumwgsjrxbqsehuxkylscnqhzarfzezsynoghzafaszfzveltr",
"dxfwggyxnxbosbdiknikukctrdrwpmnsmuoscmspmvfgzjojwytqlxlcaeaprokdkaxnpp",
"edlklmvbvtaqjlnwpnbqfserxqrudikknxuyjragkawvnjrcyusdoyulroiwyugmtckctk",
"ifmgabpugnqytfzpssfcoewvspzcttpdydjbfyxlonljumyneervkoqcfpgzkvclbmoiml",
"tcaglvvmkbqbwcroexekwqiabjorrdcmfdutypfktxlpzdedakpyaxaeirvbuanbfiufzb",
"psyckzfochauharigczedverwlbtqcwhxvjjupxzyztgzmqiormumsnkfqfvsccrznatez",
"udyplacdiswwmkqzuvpcskewddjeyoftteiegmjohfmtpcvlzmnryrncuwitmnoftyjzls",
"nszbnofkaexpvvhkxdhfyvvmbonmoyhdsgfhxksxrrmmovxmzgtxbqmefzrtzywtedcbqw",
"ahnptcksqlallecxihyzczzaseeuhwridgzykltaxtokzsjkzhjdgldapjwyfpiiwhjivc",
"jsxzexrnhsusvcdaeukatrqdcollwgnhakigjztqrploropvlbxgupjwfwhcewlgjumsvf",
"lpuwdnmukzxkfszpoflyjswuyfqlamsldpjicxfpxczewatnfhnqzjlzpdkrrdeuundymi",
"njmoojpjywslntuatlfdcxigtcvydkiqvvhlgyveuppjjllcxrfboqkjuhixrqqnlzytxv",
"xtloduaqwzhdcxvohswprpfhetgdmfamznceheuffelibiwiauzukfboaktmpwaqjduthr",
"apvlxwwvhyqgscnwqnimczicqrhmkrdlgyyfxwagvsmpucnlpvztvhwnyfzlydyedwjcvm",
"iqexhzzvmqqlknsiaspafofdskcenxsxpwwyxvtlomwazqiclzcsnjwitaogxggoecmeai",
"pouoovgyxrzbknmivgijohruxvxlbxtrnpfdnldmfcqrpcbmijxxsotpmqanpwgennhazk",
"pgnfzehatsjqpdhkuvbwkssrxgeeifrxngcmmmmfexyvaffuairmbldatkgepxbdfgpsse",
"zybxtecaaejrrmfwmygucysgbzmstgwteaszevzebiyswdridxdivxqyyetskrnqrfpxcq",
"cebcyxhpimpnwkmmlkqeecxtspzjodcqhduiabzkqoxmblzmwpscupwmgxyvcanmfiuhlt",
"sbkrqldpzbgtdaibprapmdpbpwjldxevaqnqbshctqvwqgahxawlfnmujyfnvmkxezqgrz",
"kkpgjimlplnmwtziplgxydlidpitxbuimkoxscihnvvlqxtgicdihoqkfafdcalqmbpedx",
"nsujdliytqayykoqwtrcwvejnskcwnbjhvukicjdulbsvrjslcwjzctmudqqtrbaoylzaw",
"cvhgpdzavkctwdvrppuffpyisngfmjbqeiyvnywkkadgeyxvnudujbdbolgcujvastwhrs",
"sesvkwuishevcpyhrpszrnjondilkbdefwasuucmdgjhviooxjqqwbhlgrxsucxayxuttw",
"hwetebdsscbiuzlbnrsmlnoipphjkahtznmdopxgtbqocbppukdgzsqojyztyiozvbcjsc",
"smdicfmtxgdaocufsffrafzpfwqhgkjyyoiauwwtdzvtesayxfsylrnqofzwplwqzgsvdo",
"qiqmbwecubjmbwgoowvounbqdawvyzmojealaepwiajjxralnvbhiczndxldzxributdak",
"zilkukbuvorxxazwpewahvzbdavzfvjfgwpagrwehnbhpcffjbhqwhtajozpmkwuhlupes",
"tohwvzbagkcncauwagmbvymruveqmjiixsgsrhuxrykuzhsznedkfpbzmhqyqainsphjwe",
"iqcvmbeedrkgdpxgrlnjlejuteldpjhyzjvnnzrsscyvtxbkiotvufpqjctymcylntzass",
"skwshsrkebbyxvfonorgofknqygrabmvnknvchfhkghhemyrcryqwkfoioijpuecetzjaf",
"qnlxupjujnlhfjtlyczilqcruikurnzhamgweptnegwkqpvqtwygocxikkeezfnbuuzyls",
"nszlcrczhwxfenhcvtocznhpqblpbykqqjdscgtjeqqidxmbsafspmjfquxtshkjspduxx",
"fbpvmvuaymbdgsppyhlvbeenpweuscrxfjsrgoseavhjnyangmkjqoyfmczggtdmexfklz",
"oowvzkvzzblkmbamiprkvxfbljarvosjcpgbbdaafomtpniaezkzypakaddvrvgvkowlry",
"mymyuencerbqtzhvlhyoepkmkuciivjuwxuqbkuhdxxwyesknqytiifufjdnfojdlftppp",
"wtmwrkcjuscvlmftgmelbjzmmlshcjwyekwwvbhrtlogxuzgigrkprweeongamggwdctgm",
"nzxbfxxhdgnwqenmktdybfmilinqetcrububysidyxaqepcojhomoaualjqreuiyvccwwk",
"zukzkoppeayvmnxjpiufbzbjzyobumouhavtqmkumlpbypknzeubfvmfvaiqpymwyjrowe",
"lkpclnrvcrcwshteoohzgwxsuwcnmarxkgcwvttxkxvehqjvhsunquimqmzemreyzgwvzq",
"smpqqwgbspvoflinxabxfpqjnprkkqcfcrvvodwitsyydhndjoaqdsbshseslgxnauioxh",
"yqzwoefbhrrjhwdjpldvfoceccymsvvqmuocbwgknzwuwzfnmjirzmvdqtsirnafkrhlnp"]
"cptynvechpk"
'''
