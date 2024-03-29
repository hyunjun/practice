#   https://www.hackerrank.com/challenges/common-child

#   https://en.wikipedia.org/wiki/Longest_common_subsequence_problem
#   https://www.geeksforgeeks.org/longest-common-subsequence-dp-4
#   https://stackoverflow.com/questions/6555873/faster-algorithm-for-the-length-of-the-longest-common-subsequence-lcs


#   Wrong Answer
def commonChild0(s1, s2):
    #   1. get common chars only
    commonChars = set(s1).intersection(set(s2))
    #   2-1. no common -> return 0
    if 0 == len(commonChars):
        return 0
    cw1 = [c for c in s1 if c in commonChars]
    cw2 = [c for c in s2 if c in commonChars]
    #   2-2. exactly the same -> return len(common string))
    if cw1 == cw2:
        return len(cw1)
    #   2-3. compare first char matching and the rest
    def getCommon(w1, w2):
        if 0 == len(w1) or 0 == len(w2):
            return 0
        i2 = 0
        for i, c in enumerate(w2):
            if c == w1[0]:
                i2 = i
        e1, e2 = 0, i2
        print(w1, w2)
        while e1 < len(w1) and e2 < len(w2) and w1[e1] == w2[e2]:
            e1 += 1
            e2 += 1
        return max(e1, getCommon(w1[1:], w2))
    return getCommon(cw1, cw2)


from collections import defaultdict

#   Timeout
def commonChild1(s1, s2):
    #   1. get common chars only
    commonChars = set(s1).intersection(set(s2))

    #   2-1. no common -> return 0
    if 0 == len(commonChars):
        return 0

    cw1 = [c for c in s1 if c in commonChars]
    cw2 = [c for c in s2 if c in commonChars]
    #   2-2. exactly the same -> return len(common string))
    if cw1 == cw2:
        return len(cw1)

    def getCommonLen(w1, w2):
        if 0 == len(w1) or 0 == len(w2):
            return 0
        cnt = 0
        for i, c in enumerate(w2):
            if w1[0] == c:
                cnt = max(cnt, 1 + getCommonLen(w1[1:], w2[i + 1:]))
        return max(cnt, getCommonLen(w1[1:], w2))
    return getCommonLen(cw1, cw2)

#   Timeout
def commonChild2(s1, s2):
    #   1. get common chars only
    commonChars = set(s1).intersection(set(s2))

    #   2-1. no common -> return 0
    if 0 == len(commonChars):
        return 0

    cw1 = [c for c in s1 if c in commonChars]
    cw2 = [c for c in s2 if c in commonChars]
    #   2-2. exactly the same -> return len(common string))
    if cw1 == cw2:
        return len(cw1)

    ROW, COL = len(cw1), len(cw2)
    board = [[False] * COL for _ in range(ROW)]
    for r in range(ROW):
        for c in range(COL):
            if cw1[r] == cw2[c]:
                board[r][c] = True
    for r in range(ROW):
        print(board[r])
    d = defaultdict(int)
    def getMax(r, c):
        if ROW <= r or COL <= c:
            return 0
        if (r, c) in d:
            return d[(r, c)]
        curCnt = 0
        if board[r][c]:
            print('[{}][{}]'.format(r, c))
            for rr in range(r + 1, ROW):
                for cc in range(c + 1, COL):
                    curCnt = max(curCnt, getMax(rr, cc))
            curCnt += 1
        else:
            for rr in range(r, ROW):
                for cc in range(c + 1, COL):
                    curCnt = max(curCnt, getMax(rr, cc))
            for rr in range(r + 1, ROW):
                for cc in range(c, COL):
                    curCnt = max(curCnt, getMax(rr, cc))
        d[(r, c)] = curCnt
        return curCnt

    return getMax(0, 0)

#   Timeout
def commonChild3(s1, s2):
    ROW, COL = len(s1), len(s2)
    board = [[0] * COL for _ in range(ROW)]
    for r in range(ROW):
        for c in range(COL):
            if s1[r] == s2[c]:
                board[r][c] = 1
    #for r in range(ROW):
    #    print(board[r])
    for r in range(ROW - 1):
        board[r][COL - 1] = max(board[r + 1][COL - 1], board[r][COL - 1])
    for c in range(COL - 1):
        board[ROW - 1][c] = max(board[ROW - 1][c + 1], board[ROW - 1][c])
    for r in range(ROW - 2, -1, -1):
        for c in range(COL - 2, -1, -1):
            board[r][c] = max(board[r + 1][c + 1] + board[r][c], board[r + 1][c], board[r][c + 1])
    #for r in range(ROW):
    #    print(board[r])
    return board[0][0]

#   Wrong Answer
def commonChild4(s1, s2):
    d = defaultdict(int)
    def findCommonLen(i1, i2):
        #print(s1[i1:], s2[i2:])
        if i1 == -1 or i2 == -1:
            return 0
        if (i1, i2) in d:
            return d[(i1, i2)]
        cnt = 0
        if s1[i1] == s2[i2]:
            cnt = 1 + findCommonLen(i1 - 1, i2 - 1)
        else:
            cnt = max(findCommonLen(i1 - 1, i2), findCommonLen(i1, i2 - 1))
        d[(i1, i2)] = cnt
        return cnt
    return findCommonLen(len(s1) - 1, len(s2) - 1)

#   Timeout
def commonChild(s1, s2):
    # find the length of the strings
    R, C = len(s1), len(s2)

    # declaring the array for storing the dp values
    board = [[0]*(C + 1) for _ in range(R + 1)]

    #   Following steps build L[R+1][C+1] in bottom up fashion
    #   Note: L[r][c] contains length of LCS of s1[0..r-1] and s2[0..c-1]
    for r in range(R + 1):
        for c in range(C + 1):
            if r == 0 or c == 0:
                board[r][c] = 0
            elif s1[r - 1] == s2[c - 1]:
                board[r][c] = board[r - 1][c - 1] + 1
            else:
                board[r][c] = max(board[r - 1][c], board[r][c - 1])

    # board[R][C] contains the length of LCS of s1[0..C-1] & s2[0..R-1]
    return board[R][C]

#   Timeout
def commonChild6(s1, s2):
    #   1. get common chars only
    commonChars = set(s1).intersection(set(s2))

    #   2-1. no common -> return 0
    if 0 == len(commonChars):
        return 0

    cw1 = [c for c in s1 if c in commonChars]
    cw2 = [c for c in s2 if c in commonChars]
    #   2-2. exactly the same -> return len(common string))
    if cw1 == cw2:
        return len(cw1)

    print(cw1, cw2)
    # find the length of the strings
    R, C = len(cw1), len(cw2)

    # declaring the array for storing the dp values
    board = [[0]*(C + 1) for _ in range(R + 1)]

    #   Following steps build L[R+1][C+1] in bottom up fashion
    #   Note: L[r][c] contains length of LCS of s1[0..r-1] and s2[0..c-1]
    for r in range(R + 1):
        for c in range(C + 1):
            if r == 0 or c == 0:
                board[r][c] = 0
            elif cw1[r - 1] == cw2[c - 1]:
                board[r][c] = board[r - 1][c - 1] + 1
            else:
                board[r][c] = max(board[r - 1][c], board[r][c - 1])
    #for r in range(R + 1):
    #    print(board[r])

    # board[R][C] contains the length of LCS of s1[0..C-1] & s2[0..R-1]
    return board[R][C]

#   Timeout
def commonChildEditorial(s1, s2):
    n, m = len(s1), len(s2)
    lcs = [[0] * (m + 1) for _ in range(n + 1)]

    for i, c1 in enumerate(s1):
        for j, c2 in enumerate(s2):
            if c1 == c2:
                lcs[i][j] = lcs[i - 1][j - 1] + 1
            else:
                lcs[i][j] = max(lcs[i][j - 1], lcs[i - 1][j])

    return lcs[n - 1][m - 1]

data = [('HARRY', 'SALLY', 2),
        ('AA', 'BB', 0),
        ('SHINCHAN', 'NOHARAAA', 3),
        ('ABCDEF', 'FBDAMN', 2),
        ('WEWOUCUIDGCGTRMEZEPXZFEJWISRSBBSYXAYDFEJJDLEBVHHKS', 'FDAGCXGKCTKWNECHMRXZWMLRYUCOCZHJRRJBOAJOQJZZVUYXIC', 15),
        ('ABCDGH', 'AEDFHR', 3),
        ('AGGTAB', 'GXTXAYB', 4),
        ('VGXGPUAMKXKSZHKBPPHYKINKEZPLVFJAQMOPODOTKRJZRIMLVUMUARENEXCFYCEBEURGVJYOSPDHVUYFVTVNRDYLUACVRAYGGWNPNZIJDIFYERVJAOALCGXOVLDQFZAORAHDIGYOJKNVIAZTPCMXLVOVAFHJPHVSHYFIQQTQBXJJMQNGQJHWKCEXECMDKMZAKBZRKJWQDYUXDVOOSSJOATRYXMBWXBWEXNAGMAYGZYFNZPQFTOBTAOTUAYXMWVZLLKUJIDHUKZWZCLTGQNGGUFTUAHALWVJWQNCKSIZGZAJKHYJUJLKSESZAFZJMDTSBYLDHYLCGKYNGVMHNEQYJDUGOFKLITXAOYKFOQKZSZNJYARKUPRERIVHUBPEHXMOYDAKKLBDNFHFXAMOTUBELZVBOZJARAEFMLOTFTNQRJOLVUAMAHNDEKFDSQCFVMQBOCBOMJXRQSFSKEVFXPHCQOQKBBOMCYURWLRNHRHCTNTZLYLVWULBDKCDPPGYKICHJTPUKFNLXFCEVKJEZQSMEYCANJLBESSRFAZDPRCOMDPJIMSFBUSLKSYVEERGCGMONCTCSVYPOLPLCGSQYFKILRIXODIWQCYREIWKRPIUIASFKJEXPFTZNQIBLSRJUYFSKNDAPWJEFUCDQCIUEHVFNDGHRXXNMVZLJXIOYUNDVPNDABSBNWOEYOMRJDCQCRXVYAHERMUDCCMUEAHEBYVSAKXWSEQZDUYFEZUJAFFDRSQFSEQSDFCGDENMRFWFNDIJTEPXHNVEDFBAGZRXKPRTGBOUKFXIWHFZFKSNAWGCUBSPXSIUYTQRWMVXFSVZLOTLFWIMLIYGNFDDESWMXUVHNQVJZGKPDZFJMCJCMSAASKEXTLSJRGGTYCGCQFPOQOMROUHJKNTQRYHJIFCXBYWHFUTFZMJCDLIVNUXMRDFGHKQLQZAEEAZKOOMVPYSJWNCYQYABUTSITEZURQHBUWABEXRCUIWAFNFVCASMRMBQNUPRUSKHSMEICAQQESYYVOPEPMVDOSIBRVQOGHDEIKBPQBFGRUFXDSQCHJKUXPXNGEBXRMQDGQJSOSENCRBWKNLLVUCVUBYOZFMTTXTLSRRNRQAVSHASZRENHLBZPNPJGQFTVWGUKJWSEKFCGLLBZLNVMOSMVQUBTWSGLTVMMZMSLQDXQIIFZKAQHSXZGUSEUEXLYCGUBHDNWHRSSYIYBITCOOWLHMMRDPGTRDWALVFFKNWIBHWHACQFJCMWUPOXONAVVXWSVPRPYMSKZNABSQUWSSUCXRMYWERFPZIQDZIYCNYNTHGMDAVYBZBQGCRGVWALCPTUTZXSQLKCHITHCDEZSAEFLDDFLGTIXBNAGKQRZESCKRIHWQPLFPSPKQVIFBMNQWIDBKZQIYGWFUNEFIWPXUEUMDWUGBFGNOJJRJPAFGKIRRUEOEZABCQLZMCDWMKLVYZVUUGHETWKXZUZFVOIRAREYBLWPRDNETKYIGXYQPZXECKYGYXTHSZXGYIDGLDNLZEQNDBVACJQYHFKQVLIUSQMXYEQYQORZMMJWSUICNYXQNKTYLAQNVBJLLTEXGRHIFDNEUGYSZNCRWGIDCFJGDZKOQFQBWEUCHTDVPIUNKPEHCSHTMRENTGSNDNBTBBBMOGUOPYPWKAPKRWISAMNXAGZFQSFSXTYXEPBPUMTLUJGXUENMZGGJMGIUTQOELTNLYBOQJEGCVUUIILMSBNALVBSFUTYARENKEWZLPWGQZFNNKEXXDSUFCJVRBKESROBOSUZUMUCCGMRSMXZTPSIQCHFCLVZKMVFMUSCNBRLCZVFZWMMKTUSAJDHOCMPRJLNDYDXROJJAHOCITARXLQXQJXQHPFZEWPYYKZEQJPEHSGIQVYEZBQWNPYUCIOBBLOXJXUOZSUVQWPHLHGLUFBHJGBPKXJXIYEUWMDUSFMLXKVQSMWYTKJOAKBNPGPHEFWPQNRBXWDAIPPUEOLNGEDDTRXPAXXZIWPHXKEINQSDIVGPLBCSZJHSXEICKSXBSEJHGMKIHTJCQQWXFTJSWWPTMGZPTQNOIXWPARKLAYJDSBIJTRGTXGZFCPUCHDSMKVQRHGDIIDNNUNWSXSCQQNNQMPCPKAGZSXMCBORWJYQNNOUSXHSDMKLMNDNTFUKMSKHNFJNFRVHQOMOFZKQIPTSIHALUJJXKBURWSBDLLAPWRQCARXMLZQWFCALVWXJFLFJTSTVRCTLBKBSJPNXYHSCXDXEPBWQECEWRZCITMDFBWZHIOWCPGGBUNWIOPNJDJCWRMIXZQULDIALDWRDJMBHVKGQYSPROVNZFRBAJESSMYBYCKDQMSXSRYDSKOIKTYFXJOMBTWYSKCTDJFQUVEKMCKRWIVZAYCTXCFXPTGRUPRMPNZSWUOEGWGDBBYPIRUISJQIBACPBOMBSJOQOZZSDGDRGYQYRFRKSSNTFGUDFQRQZXECGUCLNXEATMLQXSJKYJXIFIRSWZUDOLGMNLJJZJUJUAYJIICCERVHAVVGTCWHLSRWAQOTOGOKHTWGJMFQSLVHZPGNSFQHGBOEHMZPONRTKQJUANPNUFNLUEZLJSQVTOFMENWFZLGRRPZETXOGOBQRHUHLYGENSBKPWQBWWCZNXEIYOZTKMGCVJUSURKTIEHAHZRNTRRASIKBABWCSRHACZNXYUDGFPQDPGUIJAWGHWVVFOGDVTUHMORJCEOFCTZQYGFIETZKBEGKBSJZMFZRMFPMGVOAFXFYINMAYUXCJREDRYDNVLXWVHUEAIQGLUUFBBDTPVTCFHPRLYRBVVLNTRQZMQAWBSSRANJHAXTJVSXSDUOZSXLOEBLCIFBYFEUONSYRICVCCFPKZTIOALHQHQEKYDZQXMNZCAPLZLYXVFBPDZMLSFMMLGTNFRAROEBTFDUZXGPSAQWCNJIYTSRZYFWKRDLABYWHCMFGZVCYBFLKACYHHCKASMBLHBDJEOJNFWYLCQVNBMZXUGFSIYJGUICGFFIWRSZZDBZJYHVGPNFSAPUFJQFESPXBFLJGTDGSMFEECQFWFVKWEIACDITMSNFALDCQLRYCLLMCCMODLNLBKWVGMDZWAPSBZYRWXASQVCTBMTBPIDEDMVRPXQNDCAHLTGZSHJARUUEMQUXRRVTHOHCDKUURWURKWEXHYPSBUPXUISDESHLTSVFHVJVHNXGGARVCDAIIAQADYJJERNIDPERSJDQUCSAUPRZTYFOIIKLHTJSZNDDFTCGELCHWBIZHESDUXMACMZILDECEGSHHNTFZNBBBGXAVMPNFLHPXYLXKYZTWBQWPUYMQLNXMETGHTNREFEYPIVPYNDOBBRESGVLMKKXWHLOMIGIRIZLNGKYKRYMHEYWUJWMJHNZXMGMKQGSAJKYKVQJYAPLNWKCUBVBXDXYHECCRZFNEHQEIZVICXXXESNSSFEUZHSJDHXNDDSIUVXANFKPEQODIRLSYWLYMIWSHVENLIUOMFLSYIQACJUAJHXMEKLFADFVXVMPKNEDSHBYVENBOQUEAAIQWEXNQGQVJWZFOFOKVKGDGZHWRTKTDBERAPDNUMYTFOBBQCOZOJIVHKNGVYYSTJGSDFNOSJLRXPZFENFYHWAJCJUPUWYUVKORVMIUPLWVOOOJCKJMAQYSPYACDNGDNMUYRSOISLCMORSFGZZKSPOSLTNXPVOHDSPMZKEWHWNJMMMGIQUYWBYJIOWEWRVFLTAJJRDUGEJYJRKWAZOGERWKHVGTQUXUXHRUBFRQYFARBIAEPORGWQUIJHBUWQVEJGCOJNCYUOPFGFPTTEUSXAJVQYNZZISGNXJHJETOMWBTTPGBSZZUWRFNORZXTOMUWNQPKUTTCBYBDHLUVCEXTUOXMZGIBULSZOBTMXUTCCLNYXCDFHZNMWHESGEZPVXPYCZLCGYAQNKGIJUKIIIUCJFUEQBMXQNWDCYBERSZMOFRWOCLBYNJWJCRQAYJPCIJNDYZMCTZBAOQEUGWRMHPKZVYYGKOVPCKBZETSHNEBUHTMQQPMBWSEOCXEOBHDJMKFMZVMKEZWOMLYZPAGRXGXYBZTSXAEUNETDTIKJBBXUQJCDWYHWREGFYJHCTUARLQOFGWHPYUTWRBYEBFSSWBRCZWXKLTZJGMFUXARYDAGGOJPHEUSIUBPMQJMHOCQMVJOSPDFLIVMSRCQTWGXDAZUNYTIFHXQUASVCGDLOZUQZWHFSSRCXARCJFLFTMWNGZONWFSVTUKXVBSOUBBBPBFWJFNGELEKPMOADIZDSORTKABMSWCMYWNBAJXNKVMNDBVTCPNJXWMODDNTSQTHUSVZMKUEDBDKBIQDWPWPSSRJJFLSWUFMHCLMNSTZUBTCVQVQSDSSGSCJYQZWCAMNVRILESSQPZGQXDLSNCLUJDSAQBXXYLTZLQWLUORTKQADJCQUQDQCSVIXGWGLWRRMKHDSBEBBJVCGZLWTBVASPHVMNFVFJYKQMIMWXEMMAHHMZOADAPWORUVLPQOLWBMKESKAFYZBVZVMMPRWAXISDUKVMBVCVZWXYNRTKSBDZKVAGIHFGIQMSDEJXIRROWIRGQVZELYSOHWVJFALSGXGZOKBFURVECUXSIPQVRWQJOSFYBNCIHPZJCBXEFZVRIISGFIPSIAPDPBSSGLQJUHVQRXEFPTIMXEDAHMJQTVIQRXNFPOYSAKXHXRJETYDSXIXVXYUJBVQAVXZUPQPZDQLNDDXFANWNKTLPJCCPWUYGXYYXUAFYPZOAKDXPKAHVPJJFDOGNZBYIXYBMKDAQLIXEUTOJGTDJLTWPXPVUMBUDCKMDXRHQWKRRLLTGXDYOAOKDPARWBANIDRFSSIUIGZDUWZEJBBNUOIWQLSGTESHSCNVLMJYIWHAGTIMRQTFFKFGBODLWXIRGRMRDHLIHYAMXMOLBYFWCDPUTEDZCWSKRPKYKQYPKSLSQNFNDIGWHJPDQMACLGNEBLKQCEPSNLJBYOYXCHDIYYGWCHTCOXYZZBLNCVOSGCFFRHAS', 'EVYRFZJIZJBKRFPPCJBHDPBYICJMVXNSXRLFUPSNIYCHUTSVGWTRJVNEPWFSSFOVSAXKHENZIDOHUQRMXXUMFDDYGFEYPTZCOURHVEDKDOACAMYUOYEINZLVOCYDNXYKXPFKXWMDOCFZGCBWJJZRJZVSLTCPVUHZNZLVNZBDQYJXQWGBTLLQADGXJFZRTMMVBDKCZRKYLNZEJAIPLDLCTXVKLOFQNQFFKYDZGTFBFERGKEQMCVYLZQIIUOCWGDVICASICRUGGKBSRGYLDPIWKURUYIHBERGCGGXWUJDPROKXYKQQBUITESPOHBQNKQKUGWHLHKGABAPHQTFDBFHGVBLUYXWZOPSQEUKCLFKFWKXQWZAKBWBHILYFKYOIITLSHCNCYQDMJNFJEKJJDZQSWMJVNDTMYANVUCNZBDUAMHAPYNGGABONFABHVNQMKSNYHYYDLHKFHHDKHVSUSNWPPWDWVAYFKSMBSXUJUVLAIGWMQSNZYTVWBPLYYDSPRLUCGXOAAJLLVQIIHBCKZLPASFSNSUSYFHBMCBFOSTWISFNREQQYTKDCAHMKZTUAXOJIFTFVWWVMODLJMNBJEOIFEYNMAXZKTXXPEDAGSNZUVFRKIGJDCKUZOSKNADBFLGISKPPHYGXZMCMFAZJXAZHBQBQRREZXLNIOKHFKKPDRHTCRUEQXLXXDCVJLXISJXAWESPGXOXJYGEOQZEMXIKVPQRFQBXYARJWOJEKEXBQAEDYUIPLLDVKYKWPWMZHEIQGDNKSFYMIUINMORLIZMXMLHXSJOTKROYPHYKJHRBEXHAFVCJETIIMMPQKSPSPLOAYAPWBXUJWJBBIHVGVKDCFPABBAYMCZPIMZTOQBIDTJSDNKGUDECSFSRREZFBTUXIXJKIPXTNCFQUQDTANIWLEVDYODLIIWUVBOGQZWWPURCQVRYSJZDBSUCBXNLKFGCVWAGOIQIGSNVKWEMYBVXUAERMVJJLDZSPJKPVEOFJVPVGVOKSJYIFNLGBRUBYVNDYNHVLUDRYLJRGBKYSZBXNVDBYAHLZTQXUIBBOTBFKHSGYKPGCRWLMXZMHIOVKLIJTBUTFDIOJSCLMCJTTAFLMSYDWUNHEIKKSKJHXADKTUYNCEYAJDKVEIMKSQWLOGDYYDDKSRARLPGFZZNZUAJFRFEUNQJUAWJHFMARNJUIYEUZTDVRZHCEZVSFKHCDGTTNPFNKHSYPMXBOBNQYLLOAKFKNOYPEORITDIQRKMJIFOUEIBYCUXNQNUNBTNLNKCIOHEFUQCYFOBIIYBUWPRQRFOKONIRFILFQGJHFPLYASYJMZQPDWTSBKGQCYUVTBUNQNHNAEFGPJNVAGTPXFQRGMXTSVAJTRPBDBNZQACKJDTAMMEUASETGWFZWBYSFOMABHMXHLNQTBALMJFHXROGODUKWEYZMJFHKIIATYPLTUNTSXAJRCDZFJWFXRQWHPOSVXEDXOMRDMBQHAVOCMVTKGGPULOVCCKLEYCFGTYPCNCNHTWUWRMZJPBSCIMPXCZRPBIXQVAMEGSEYPGECDDFOFLQTASXNGKYWTAIRATEGYVZXTTVBFDDKWXOBEZXFNWPZXKJCDPNLVWOZNDNFEGUHYCDOOMTXBPIQLQWOTOIBBQZWXVGKMQWOWATZOZGBTRDKNDCPIVAILDYXKKNZYIYYTBFLWPAITVIRSPTZDHLFSIABOMDXQHTFNVLEUOUKTABUAWPRTURPUMHGKBUACFFFOXRIUGZAQSENYFNMGQJMSJVOBAEUQKGWPYVWPAFBNXIODTCEMCDQAXVLNYCQYVAXXYBHVDKHIUHPVUMQBFRYWTQKUVJJEAEXYCJZHRFCLDUGQRVIYLXUBXWGTCPTVELFADQXBCVTSEZNBBUAEUDGEJCVYTASTWCZYJQHGLYHZTGDDICBNLVYTJHMHENXSDHVLYFLHZQSOIDECOJQGXSQKHVFKPLDTOQYRGADZGIOOLYNWZXJRUIIYBWCNWAUPWGMUEQDFYVSVLBHQQXKCEEBMWQJYPIYGYZCDBZPKYRHROJQMQSBJILAMAKICREORUIJZRHWWFKBVZUAJRSCCDHBKUNZVWRHSIPHMBDAMNNQKHTFKYQRDRCEXZFTUAXFRPHOIPMZXCZJCUOQCZGPRMZIOTDISOSKROXJKLEAHTIRTMVEUCAYQVJBJCRNDJVXVVOUMPCGCZWUMAAPDEPSHNAIMATOLVNLMEPBJZWXMACWILFYKKKUYSUCCMFTJUOCCUPAGBYAKRUGNNSGRVBXDWGTQZZWHBKYJDKFNIEPBOLVIWSBEVYPMEKZMEVXOHKSLYLOSUSKCVEHBYRRUYKOHNENCVYODSTLPWDWOOONHNIYEGMYEKMTOPUWYKWCTHHDWZQXOCNQGZMTCTBPUILLKMAWSSJTRGXLSPQQYCZVKHHFCUGLIDEMBZUNQFSPCPHJQTUAYWQBJJSQYDFOJZOFIRJWOIOBXHFDIMSVISXEYYRKSQALVHUQLQOJZVDMADAIUKMJQGFAFJQOYWDFXPMBUOXOEISIHWBLFTQBSBCMQSKWMHNWOJRJOOAHBBKCVKSOGUCZQZVRPBMDKQYICBHJAZSCXKVRMBXHUGUZXFEJGUIANOFATRARRNZPYVBLJZTDZLRFIZBLVXKJRFACEVLDDQMRGZYUHJFBVPVLZJFNBKPKUFNAOEJEQNSNKITMIGJVIBPVIJTBEVSSVLCQZMSHQNDHZHXGGCTDZPOGABKKJTNIXVVGXHKRYILLFJMJHNKKDIQWGPPVJVCBWEQOVKIDJEBMKOLZGSLHMRHIQGLVWHICMTOXPITUPETITSOBUIWYRKMZMWFMSGFOORVZEBZPVBSCVETJKNHNQTJHNINAVAWQHPKHBCSAGDNLYAADUSPPTMGECGCBYDSMNGFPLHLMEQPDUYJVIRVRZFBRFMQKEWXOTZGTHMVBXBNUYACTBIRPPWWYMERCDUZTLKJJMXGBHFINZEEZPOFNCRTDYCEPYBZWNHKZXKNJNOTDVKFKXWKWOBTKAWEBEZAJMLPFUXOAQMEEAPDEWVJDVHMJIFZVPJKAZWPCVLRUWWXATRFIEKSQFVFIGJWYTMBMLLCQPQJNELFQLBCGLODVHXBWJNTQPKEMPRBWNAVCPJWKCIEKOOVBCMSLERUKVJCQAIXQBCHUXCDIQCSOTCHLQBYAXHWAJAFWZAQMHRTXMFDIWFFYQTVVSWXGIDAOHUHDQSYMOZESUHIEHBBCHTPTSBKBWVRSVNDQYSXMWNDBAECMHPOPMSAUCXOHITLWDNCPBVMKCUDAJESJBGMVXVTPBOOPAEGUGLKUJIIZPQPQVYPIBOOOBDOJUFCVEWMZMADYLIHDJJYALDZXDYNFCKNHQBIJHMAJWMYIYKCNGPRIVZMOUZRXRFVMZSDHAQJEOGJYEJIWHZSEHQVUBFNEFKFLTAFNFCDXNMJIXQNOPGMYVZUVWUFVKFXMYCBBQIUBWEVLYJHDSMZEDRJWVLPVCXJLPNACMEHOWHRJIEEXEAVAHUQYRYHEGRGDBHSGQAHFIIHVPSVXGQJRGOBNTLFILNFPMIDKEHUQBJHCKHBCWEWFAIILHINFVDOJBDLPGNPRTORKRMMCZNCYWFYDRTUYOTFRMZVPHRKKTERJKIJUWCVJANXEQWCUIXLWFUEGNPHHKELAKDLTQEEBMUUQHEJPOBTDLYRFBZGUOKCWARIBQJCUUBQLYRUMVCRGTEIYUDJIDIPZNNGMPNFIONDGFQGPEQPGEKNHEJMNTASLYRZUYKRIIERZLIDIHPEBYIBUDVYNXGVVKLOQPDVRNYLINDKNAEHTDIOLSUFZGOXGOFOFURIVLOCFBPGCYOCVBGFMKALQZNBKWNZPKIQWRLIMNKBBXJPQHCTUXAHUQTFBRBKDAFALDVVZRRPLOEVUCBUDBUUUFWFGBUWGKAKDRYCBVLOSSJZHSCYIXWOYBDUWSBFKSHSKVZLBNDNHNCZSKZNQIUUUYNVRDUPFJORXZDEVVRNGHYBKQEANYEYJDCQXPHEKNPAKRGZTODMNJKQZAICVLWCIWYDFSRDDBGVFKCOCZAZKDUBFTKLNYPTMRKJIOKPECEIBEABQGCKLJYMBIACXYPKNGHOKWBIPGLAXBVXKWCJCDGHCKWAZBRDFRNTZBZVCTXKTQNXTNGQWVAPWVLZXPXCSIOJWHWTZYXLZUSVTRYNJXQZBBVZXFBHJCDAWJAUJUUGLNTLCNIGZINJUAZHHOZCTXPCRNSMQBEEZWHIBSEAFALDETCFKCVLMQCCLZIVVZUMHGAEPAIFGSCINZQJEDNTSYGVTWSQWREKGFEUSLRZYXXTXABLAWYWMPYFXBIGRRITWTELCILVQRNWLJMNBSCILFZOUJGRGQWZDGXZWSVKVWQTMUKXZDCYDENZNEIMHXWYATJEMDEQTXYPMVFEKHSPZFXHYKPGWLSJCDOBYFGEUGOVJNXOTXKDHJTIFFTJWHHDXCNWOLPHGOHJORXKQUCTLSDMGSVRDUPWVZRUSEDIOMVFSYERIWIXVPSMHIISMNSWPVAQEIXIRJNABCAPOHKXTFXZANQJUSTEAOCTNXACBOTRLXHGLSXMHMATZXFLTFJDAIYSQSZEJUPSBRGFEGHBWIJAVFINBBCFQRPUTGARLCNJYHZIADZPSUBZPEYPEFLUGWPGIFNXTGBJCGRLVVBMDKLGNYPLZBXZQSSQYLZZTKJLNMXMSLBOCOXQPGDARJAFTDZCVJSPXXIZQIEHGYOBWULEYAZGISEMUWVNCIPBDJCLIWBCPKZKPUQFTITGLWJTLHALWOUYGHRGJWRCNNRSAELAKVVUXUGYMUKRJBYFKYENHZBDTQEBVLTGLCJSEJWJUZCYNCMRIUQNNCNIAGCTKLFEZDFWKHLPIWZCZGHYCJLJQWVKMDNBJNKIZWBWHQWPPJNREFYQMCDUGXMDDRUAYHZUNFGCKDDZSJAKIEYZCZRHEFNJXLISNBITZYWZEDQNQCPAXPTG', 1618),
        ]
for s1, s2, expected in data:
    real = commonChild(s1, s2)
    if 10 < len(s1) or 10 < len(s2):
        print('{}..., {}..., expected {}, real {}, result {}'.format(s1[:10], s2[:10], expected, real, expected == real))
    else:
        print('{}, {}, expected {}, real {}, result {}'.format(s1, s2, expected, real, expected == real))
'''
HARRY SALLY
 1  4  1  4

AA BB
01 01

SHINCHAN NOHARAAA
 1 3 56  0 23 567
HNHA NHAAAA
H [0, 2] N [1] A[3]
N [0] H [1] A [2, 3, 4, 5]
 NHAAAA
H o
No
H o
A  oooo

ABCDEF FBDAMN
01 3 5 0123
  ABDF
F    o
B  o
D   o
A o
'''
