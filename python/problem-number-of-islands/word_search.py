#   https://leetcode.com/problems/word-search


class Solution(object):
    #   98.02%
    def exist(self, board, word):
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
            print('board = {}\tboard[{}][{}] = {} from {}'.format(board, r, c, board[r][c], s))
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


board = [ ['A','B','C','E'],
          ['S','F','C','S'],
          ['A','D','E','E'] ]
data = [("ABCCED", True), ("SEE", True), ("ABCB", False)]
s = Solution()
for word, expected in data:
    real = s.exist(board, word)
    print('word {}\texpected {}\treal {}\tresult {}'.format(word, expected, real, expected == real))

board2 = [ ['A', 'B', 'C', 'E'],
           ['S', 'F', 'E', 'S'],
           ['A', 'D', 'E', 'E'] ]
data = [("ABCESEEEFS", True)]
for word, expected in data:
    real = s.exist(board2, word)
    print('word {}\texpected {}\treal {}\tresult {}'.format(word, expected, real, expected == real))


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
