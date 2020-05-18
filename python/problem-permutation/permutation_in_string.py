#   https://leetcode.com/problems/permutation-in-string

#   https://leetcode.com/problems/permutation-in-string/solution


from collections import Counter


class Solution:
    #   Time Limit Exceeded
    def checkInclusion0(self, s1, s2):
        def isEmptyStr(s):
            if s is None or 0 == len(s):
                return True
            return False
        if isEmptyStr(s1) and isEmptyStr(s2):
            return True
        if len(s1) > len(s2):
            return False

        perms = []
        def perm(prev, s):
            if 0 == len(s):
                perms.append(''.join(prev))
            else:
                for i, c in enumerate(s):
                    prev.append(c)
                    perm(prev[:], s[:i] + s[i + 1:])
                    prev.pop()
        perm([], s1)

        for p in perms:
            if p in s2:
                return True
        return False

    #   Time Limit Exceeded
    def checkInclusion1(self, s1, s2):
        if len(s1) > len(s2):
            return False

        s, l = set(s1), []
        for c in s2:
            if c in s:
                l.append(c)
            else:
                l.append(' ')

        sortedS1 = ''.join(sorted(s1))
        for i in range(len(s1), len(s2) + 1):
            sortedS2 = ''.join(sorted(s2[i - len(s1):i]))
            if sortedS1 == sortedS2:
                return True
        return False

    #   Time Limit Exceeded
    def checkInclusion2(self, s1, s2):
        if len(s1) > len(s2):
            return False

        sortedS1, cd1 = set(s1), Counter(s1)
        #print('s1', sortedS1)
        for i in range(len(s1), len(s2) + 1):
            sortedS2 = set(s2[i - len(s1):i])
            #print('s2', sortedS2, s2[i - len(s1):i])
            if sortedS1 == sortedS2:
                #print(s1)
                #print(s2[i - len(s1):i])
                cd2 = Counter(s2[i - len(s1):i])
                if cd1 == cd2:
                    return True
            if len(s2) == i:
                break
            sortedS2.discard(s2[i - len(s1)])
            sortedS2.add(s2[i])
        return False

    #   156ms, 19.19%
    def checkInclusion3(self, s1, s2):
        if len(s1) > len(s2):
            return False

        cd1, cd2 = Counter(s1), Counter(s2[:len(s1)])
        for i in range(ord('a'), ord('z') + 1):
            c = chr(i)
            if c not in cd1:
                cd1[c] = 0
            if c not in cd2:
                cd2[c] = 0
        #print('s1', sortedS1)
        for i in range(len(s1), len(s2) + 1):
            #print(cd1)
            #print(cd2)
            if cd1 == cd2:
                return True
            if len(s2) == i:
                break
            cd2[s2[i - len(s1)]] -= 1
            cd2[s2[i]] += 1
        return False

    #   https://leetcode.com/explore/featured/card/may-leetcoding-challenge/536/week-3-may-15th-may-21st/3333
    #   runtime; 1384ms, 20.37%
    #   memory; 14MB
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if s1 is None or s2 is None or not (1 <= len(s1) <= 10000) or not (1 <= len(s2) <= 10000) or len(s1) > len(s2):
            return False
        c = Counter(s1)
        for i in range(len(s1) - 1, len(s2)):
            if s2[i] not in c.keys():
                continue
            if Counter(s2[i - len(s1) + 1:i + 1]) == c:
                return True
        return False


s = Solution()
data = [('ab', 'eidbaooo', True),
        ('abd', 'eidbaooo', True),
        ('ab', 'eidboaoo', False),
        ('edb', 'eidboaoo', False),
        ('prosperity', 'properties', False),
        ('adc', 'dcda', True),
        ('hello', 'ooolleoooleh', False),
        ('a', 'ab', True),
        ("vxqakfyaqahufxfizupjrkkifjlbfqfeprqrfjvxnubntdtlvz", "oumgfmlrbivgnrvsfslnheghnbhhicbvaddqadwicekguhjairhpqtebqvzyxdfodntxmoqtffgmsomnhndbrffxmuyjvqazwfvugyvmshxignfenmkihorjkshwyuxxkxidpkalqmdnxxmnovhangcwggjwjrletxhelehcipflvqyueptgjxugyipegamjbweqdfeswrjepjjlviuhfikfaojbhrujdfpnenrvajrdplwaevpbzkcdkyhidbgizwofjoxfvnkzhmwvegnfipgmnikljmmcrleffceqsxrxgsjmjmaflnxtigfoeaafsrjaxaqumhatpdeueridyxfjajsjkcrfwkwguclqtrefwevwalmcvoiragprwwnxpwgqoyulsadfhstduevikkkwmofklomdvpdcnxxsotudmkjgakbzopzengbfrvhiikzrsmmurewnnquydhntpqprtyvouatjevvoerbnzunwtdiigohcctulnvpgfbtdjmjsvszphulflmolunohifxsycaiifkngpuycnlihebmhaapureljxlqozydijsbcitfrdjhbdppvhpfjfuxujwfkcezyvhbityajxcccbuyvoluzndgjsyvrbluvagqtuujpsxjcgdtkbhaxsatmellmotdeoxsxjsywuavjqpzjkcpsrowqgogovcouosjhblhdmbkeidafpimjaiypownlcilpahbszmmcwbqmztpdmbqeuizjwdifruojquahdtdukydxgehpourjytveajjvtpiphihkmgqpmnuukpqtjyyqhfsiezugszdbjsseaxxdxomhouvetgcvfeuvwszmhgpkkorubvahxoufpfcukgchdubddpijsolrkvgiizhqefdhvpzvpmuxnwpcaepnpuicgvoxdqfcaabhsxgnorbpkboueplrpztqehrufldndxuenmvynranzqontfihfwvtxmiadbogsawlpmyycaztkyrqxwoxocbtngrmaiyafqqornrknnsmulglzyjnydvwpfefbuwhcocvyczklwywgwergmboqagcsngavorldbpsefoaynkmfqrjzdtbylibwwhhuhfqkoorihjewpcpuxhjnbeiegpplsyrzzyxsnnslvbkslzhwqjzrijdyucnnoshkxbagqdzxwnarwbzivhjpzgvaqrtywqwdetcqtsxviebsnpeflvegyjgxaskwuesfaqdjfdvuklayyekvumbuciranyvymtwshowdxyxbtpuchskraonnwvvvbdehhjdqiluauesssredqoeypadjsahxjqrgxmguppwrydbsiuvhjxyvsseeisbymztpaxclvxsvypdnabnhcnlzelogrfcvvzpwrujkdvwvzlgdbdqgiruxygolkamiluvmfuoaslakmsaehubjxlcfvonmcnqenxwjgypqfedszrisegdtlwhxdsqeyhkynmtdyrjwwslwwtucbtuxxlkymelgqumhgyjnnjtqvaatmcfpbupfszdcuwgbyudffdpxszrqskmnpdqeauilbwnojibjfqwaalwnmevjbbzvptawuemsvlqfmonxycnfnzmgfmwpmjcyvhjfjpyhywjqbtjwhxudqhuclhyfbiuazzvnklkjfiupntduclftpddhfkioqkptklhynubibyjwllgexbjafcgubnelxzdapnxsqtmnqcdscrgpawigubbugtnxvebnrlujkxranwzbiemsvykjlmnyyfkrplutmpohohtqntxmkdfmlwvspedxlgylwbqfbhtolkfbfjfmvbhxafbwmlolagckjeffnwsiesgkhpyeupuyvcmfhlxygrmkkvuarjviqxfgkwturzkzwquefcyelduecwqrachowsxbdcgrvtkmlkyloqjjlyctuzsztafqearzuiogjrfqbseqibzddpabbfhbkeiorgslhecyicrvxvlzynxctnydzpgghjocuqimuxlvwymkhvbaqyljurieblfffxplmfwszrhvqiyzaqruihxvabytqvhmauzmrgcxtiotlkhtqcrugthgerkvixykexnlyxntpgagigdepzchsplujazcqabzvjcvutxriirzeydvffvzhhhihlfwewusmuzeecuytcwermdxpcffsewvyfearxirlmdwqfxsaljqnyvfiibqgxpfgkuoqadxcbdgcrhhrhvrdluzlefeerwhwinuqzuwuvairwqraajnifdihhzuqtciqmkrxafiuixbqacmgxfybmdghunmgwbidvanucokddovmznczycruztcayuwafcvjnqxhzarfvdqfounjciebxngwfwjknqmrappyuiewzdjshsbespzfcrwswtpayqaldwdvwiyoullwxshgzdluqbwecxkiyrqrguyepbcqzgafvjfxkzvglnghbmogenghozxncfenobraxqrhybxcoyovwreawnxiurnggbecnybohhicmvxlexizgvskafbxabzkzuvbrksbanikuewjgbkwcxoqibcpissudhljplgqifaebgxueiukmqxfcjwkysjjyuamlcatwqfhltyrwjdutbqoclvpcyhczybrmsatuwaswlziqqasyedtoxhmhktrjfwytfhxhncwiovjbpimtjpkwmxkalmxdjkwqhtakjraqiykrrmgncirghthsyfuhubmkhduibikgkorispskluycaepxdgxsodeqstbreyfuxtwksqqyqlvzvqtnoirjujqeltakrbiubuoqzyorkgcdkormvctirrowpemxtfgiqpzkadbpxaghodshuxorilbjxfigpcixuhcbaoulyxaoweiaojcbmbptwcfzgvylwcfyvmhoepvexcmkqvlrbknbhvctplytkqjjvmfadhksevedhfhmbhhqzgooudgxuazdskajgvuejhpvgngpfsayyyvupptpjvveuwrsrdwewhwivpmojlvvhnahpqwvrspjpradwkylbsketjriqqpvhhedbhkkvswcvwadunencyxtxmindabykaqoaoeifqdwihohbueikhixdfumrldazczdlorgtcwrrylwjxyxzgmdujwiapwpzrikupdeijmqrarvwhfcgzrkysnwsjeqhqtembrwkcjxtvjwwwkarolvbeczwinodvtgvbbqdwipckezgxwdizrnaxfexnjoafnrqxgywruytmfktkoygmbdwogjfjdvohglnxngnijysafyrlzofdovuslmcnhxfjjitvbdvwbluorpwtmtynrmzjrbiaqvzcqrxppojxnqfebtwpmfvuhigbahvjraidtmmceaxctnbtolhuiqcforksdbypcvjagrvsqguhgbyqgqiruvvqszezfmlntffbdrlcwyjcgriqycabijkokoqzntelifjxzyvytnbfflkoiipilzafyicgniewbuapmfzqcaximlfjhvuurfscozgpgghvsuvpqqtsojdphbumqrluvgnbhlymulcmqziytcampdpdrqvfwxygwbysofektetfrwedzklwgtjytibpdzakxjfvczcfxtdjpbngqzrmvyudslvlqsezwkqkkcbxoipifopzynllvbuujssspdsycqbyvdlgoauisrkvahwipcwukmvllgsaijkdrpuxlzyzsjabsatdgzmbebovnlydvqgjphwxqgfzaqyxadgfdmtbbqlpvciucjdrhlluumnqubughdaauyhkvdekpoamoliyttnyondnmphcesvowghyktattrxhvlbdlrsfjssflnvtyltawmuqoofhvvobkistzasjhmbkessjtditkmxpzlskojwokiatbwhdzjbzbsqkzmnzvdpyaxygrehqgfqqaxnnerizmarbooohufcdhwpvsulsstmcoivxapufjqtnaviffihkpyrbrzfjenqtxlxfqkfjvazubkrdqluffwaluvqilsfrqrdmnhdhrjkbpkgtkznoqnvpswoyndtqqckqqtcubtutrbxrforaitavuazzugvgczvsyfvqnuakykuwczsithogunmpejpmrxcjjvvzbxzyrltihlsirevhjohihonylwsekburnndcwxkybjifubalefhmiiitpqqzjjazsbfgtxopdjvbdgdmcfrfiebeopggbukfxxxcjotbiltihiddnuwrlzvrzsfmgkrulvcwbeqnkkhgobokkkspdzomfgvodqvzrvajlanwbyeioxtxbyfrapsjtgqvqzdoerwkfvzmsbzhumuotznpiozkvodscfaffpgiapftqlrthudvgvenfzyaxaummpmyhyuswvegysoppwnysdpqyzzrubdrenplyiqmmvthtfreynmltqbizpycniwwnunqynfyeigduomqqulemmdjqpndhuxvmizutfzxztrbavfopefglqyvrqwggjnrpnkcyghelmcnmtmtzsepopwzoirjcdjenpuqpvutueinapitkhsmmraytgftzpjlekyhcwdltjjxsycydcvfmzwgbcxcoboqcbxzkszwlhxgpnpynjjhaqucnwhxhoyhqrkeeqgggqliogjuqyxgzcfvhmtkevipopxmowjotswevzmsxngshovradrjxihwbnqqpuhobnmlfassydwmlcgirrhrlxhkchzwrokrllbibjecgqfpttvuerckuegvooxssxvdcemgbuuirzfckxnxwsszrpcuogfuusrplrielkgvhvygnjkfzfzxsqhifoxctfhuipqxctdlvgdkewprxfuxsgfvfqtclxgzsadtvhuvpqrxjjjjrrxqgovoyuipqnhosvoufbqvugpplwzrphrjrnrllxpoxtuwlwkzotpebuamennaapntnneyvhahgxdbhtbqplduxaodhsskkpqynrzonhagrwxcoeagawjvcucsvbotsaelkywjoyeehsbfdwgoqnyyaunvhqdjvtsbxbbbpgfxnngxmikrrgsdbsokwdpyevqoplxqudieqpisrsbfxugybymbjwzoyevpigikboxhdntktxmzvjzywtbvcjrhuhwosrijcqmkfjcqxbitntabzbroolnxjllqfnznkaystntwegkkofkxsyxuamsxpubavzwfoixtjlluujjwifajginhtcywidlmkkhysmulzvzldxwyopdodzryxpkqrdukecragplzfysuwqcqaoqqfjuyfqliwkmvwvfubcklvdhzutgtgumayojpvovumxemspycidbnnmcxyarkxttcvqqhomkilqaqoovnrqlvubeeofiwxjqyayzcycgoiircgxgzhnqrbcgkrofcotpkqouabcqbdrouxxageejbjlfuzmbmfckrqbbyyhzvjrrpzbefamvoufqogovzaokciuzmevfyuaaypyjqggwipkgzkbmlbafbzlljsfmhscsodcrbbfylkfyqxokfgolmosuxpdsjspfciammxqirioodfxngosyzlkltpmsxpafmabupevthayfxdbiovsqxkrenmfkoctidrdqinrqojnelptkuzrcebddkboyxkhrfwrgvikyrvjihcfitdhdtexfnxtcsgmxkntaimhvdrndqprsddtqctysmzounvmsvxxhwgoxegqjqtouwapoxuvbkmpriuanvqoxorjcpprofqdspoosgmmlnztpaubosqqknbbqnhpyyubonpkwmlowfjgpmtgzlqujxljdadtosbhnmngepkjlmvuescozvzclobocahnkyplhqstopknrhufneybwebebhgxvwyydolesgbojzvvndmsgbhxhoybgakgdesrsmvrzhmijyjytdmpdxehxrhgsyiedfrxlgvxpxwyjaxjowwnuujnabjqcylypgduzrwituqvwckkworwlkcluicfwgydzothrmcisvfrhgpnpecbhxisfzchndxftawqybqnfuxetoupeplgxatqxytnfmokteeqmxjemgwrufklkwaxazzgelzfgglhirzjffkoqxmbtwkhhbodamujvwljmlivdbbirtubccsgrvkylyfmppilsxezcdozjpbdfjtnuwgfsreodmpafkzclgtzrgvbewdbaoephgkmwwidfcvzjkvrcafkzfdxxxdpgbqrybzejaaezxrwpxbeziscdwfbfahiefzokbnhgfqxkbcuixenmmnvolepkzkpeasrygpyoummmsoticswegyqyxkaqscmrtsnoblraczloiqcznabchbatdicakdpulzkddhcagdeogibasyddubcezmztaukusexmsjymljapvllrqfhpgkfudyedlcbhwpfimlplclrcxpttnxamzucpfagisbajnyrzvxxlzjolxxisexrojzwcratimkamjliplucbdejtcgwryaweatwbkqardkbmrdbdseggojlslcjhmcumhxikgdzxjuyyjcyyvkvseyvqjewdlrrpnwxltnnedjupeclekzyvoormnowjkrpuwfavricrvjoqqbjqijpqlmsnwmonmbjxvbpokumfvdfnxbhxxsfzxcozwhzmgrwkdczrcigxbuvlnyyuvsraobwuznkxdizyqifjwgtwnmxunhukoeqpxafupdxwzfymwsblpvyyktdspctcxmwsxfqgsgedimmhcqjztpmrbavhogwuhzbngycbggsoakrvuceiditgcwxaopcirtivcibqpxbqdstcokmypyuzlaowongknpzitpdhjkoszoqvdgrtqvckyjmduketumefixobawbekqfrnwebsijgvihedwmegkssznkwgwqgavcakfhdwesqyjvotcevhgltzcknzqrindzbywgiibjsnvsttugwizaxayngnmfsmjopzqygphvxdhdwnrnksdqwnahecbzpxeetihclinvbxmrpoiynuxsyabdmhtaqnjtsiearotujspwgmnjoqgeqbcrbrmssjtbuqciflfjjfxkiapfttwymziapbxjenhwrzcdrjtjudhcztpwqungqidwzjhsgwlxlujrpeepubglthkbnhbdqwwlbjbnndfjupllxyluagyieeurajyhdqcinkmosympawgreeihdjcfggtomoeooqbklqfxoavtpcdhrlcsezabwufygrghnmtdvisfrzfjmmgnqwnxdyvidbxizsunzosikevlwzgrybbidzyytsaspbgbgzrmgimcmmulodqbqljxeusveynagjkphulpqnqkfrbjcvtntzmjwsfifmhsphicrtchdydlklhrdghmtacbjfktgvphhlhhkkcqkytcfgjuoblfdjpkuocherhufixafdbgotxrxrcuohgpxpogfggvkdrkixzfkahtnwhvbntqbrpqxvutbldhrfirzxfupybrvolteycfjkdcaubwtqomzfepcevmpecqpteevaubtbchlaakgqpzvjwqxzbcneektiwhvyoexdufbirqhukdmtlfqtjhboncqciumvxccncrjpecyuctxfdsekblmnpmjkotsfopoeakeetsvagoayijofejkjixevcvopuymjxdpgrjupgbpjpqacdbbcpzuqwaztmxfriypcfdybjamjxflzinuxcszriqnsokpegxzfzgidrjsbfftnzxgcxtbrordopldbrtxqeeeeiixdnedgoaohbadmrnstciefemzhepbfwccdulrgduxhebifzivhzgiueajetcrwqvmeailiyyjclgfeizotkkjiaedwsqsngsoqrpekysgzlmtijsxdrcpjchecchkxhjuyevtdlohohbgrkyfsmygplztmvrgeuqjuenepnsarcopkadsbvvpzmcacliqagsfvsfylfoinibat", True),
        ("voujinkwlkydjrmbehskvlulpwmdczrzefahwvyakbzjvawxzhqztqswqghubeqhzyuyufiwxqxtyefgxteihyprxbwdykssxadcybtcverkzifjlheqwnpfeckywhusbmqktjhjjsodaqzdsghhaysoilhlqfbgobbwztiouplfeborkkqpqrrcizyazsttjjyaonwsqcbmmafafsvqofypdxcxsjqufxpxokkqftvneezbpidaqdwiprzztzlhdnyxjzpfplrwksetmdjsoskolwammzedrgwbttgjiznopuuwbqqwlyhrpzrapujnyufljiuwjaanikjsfaohejygudydnlaiczmokjqzkxxdsaexxlddypwgfopyruqvfvawqhxvwwmkiekvkkmojunjzxwiqkigohuwtlqhotzrbhpbvxpczmsqjlhmwbfyzlhlpjeawcxkracgjqmcdmtbzvssvgnuhwroxgoihlgbaxmmakzxxsyvscycylsbaaemmsrifqfcssdhzguueblxomruathvmybhgenytgddikaaogkwssdibperbodtlerrnkrdqicgnzwfxaoeqmfovjfetzrvpcsgpeeytxpbtefkwjgmuydmebhxwafemwlncgkwayljyatmmanmpfakwdnmvjqppuknagllcoyixpykxmvykfrfrwmiitxwvzwgiikzwhyhekgsyqivdizzpemotanlmtofjlcilwntqwwumgamtwszhfwcicqeqbxlpaotqfrgbehfcooooreeztiznxevlnkhqhtoeabvuzaxyslvtvelysgashucyvocysscbacshieepypttkkgbyebsrlbyrbsdadnunzzkwbyzspxucoblwmkmtnsatssazxwivfzwifiecrwofdbcaazxdofglusktgrjivedhokzdvdhtreingnglymhujlxrakfesmtemxildrpxazibxxndxctkpvupwisazhbkitwmbejzhzvafhtaisvjjvzyivmdghrmduheifbvwwjypbcxflesxswzybfaauzklcmjfzvcwulzemnaozqvprubrdzotggqkbwfjbsiyacsqyrnqdthyhemowcbxdapfuoohskvnyjehjzvyrzgkjeenfxurfalblwaklfevbgeiniihdcgaskpaqkxakrxwtklffhfvgoetfxuvpjtstdhcuithgsgdtqwuqbwjdjxctttmfrhkliyaylsdvwzyrtwenotyfourzhkqidkzmoqfbpwnodcyjnsbksbqymnvuvudsqwfnykavdpnyszbwofjxdjfhihztefusfvjcrgmoehigqsqhhkfcaumjgxzjhinydrbgapdrnzxcljdjzlwfliwhbcvoajviehzpdvxvigvaxtlctrtsctcaizxghlukazxjahjpmhwbcdcqdmvdadsluekbwwhzxrqwopdcecvpryeljmwzjotlapnunnpslbkehezwztlcauadepikdljsunxisiajtiqtdazgtizxmnilfrvhmyojdddxzsuzfychpysdsicakzctydwuwfkehxnfijhnwvwxaundogctgqcuuqpbetoqhwvgrqslrlvtlqvzuqmllvcpuikqrqfivfcfjvfohzfmvkyqbcahaarcyacidsfdobrbgclxkuijwdaaxpdtjbzudxegdijfecmmobkqeioogpthtdpvuzjqciiyfikvgzbpozxpksgnfgmrfqqcufjuangtaayzrqnhhgcxrjgroqltxwzammhoxfcykalbsutmwptspfcriqbhsxhjjhqyayquztgpsjvxbctfzskvqnsaiprqqtfzlelkgthqfpbwyjxiddryedqejhjrmzadkzdcpcekvuyyvhwqgadsgrdvukdypufnotfutbnnvfntzqgglgbfxtbhzczzfhcyvfidpcpchysdbzoeodexitmbuksjbyffpxgvpwfpqkeccxpjweokjpxvtsutezxyqpbsxekeacpxqbuhjcbrmprgisuuxoxehopkhmaqojxvodzblpiegmjtrhbijhvrogimhdfzoxpnofyujwqqzarheceiiirmuflxhcfjxqmadisviqjfzkmccnydksegmnwfdxxbngudcwthnbhockycjnzolwpxfkljmffqjoljsqcorbciunavkgfubnjamqspijnoabmyjlrtkefaiceufpffvwnygcxwrthyqerjedqyvpwtezyrvojztrxcxqqywebiqxcmnzuavbnpdyigtsyeojvubqhvetoocfifxqqczmnhmbxcxoxfdmjopbalqrivjkcayonnolylghzkajbxnxzwmnfsszryatbdhlhmoobxkxrwiwuezhujdpvqhohuevcmmjufkbzqriivpxvgvvjyvaipoewijpptjgpzsetuywcnfljssallxikayhjrjyedrlyboracgykaooieezeeubbrzsvuovdprsjifpihmuwwrgjhufsdwwbhhrloolxencdaiwhwrmsaqyamuwmicdzoisnydtfnzwrwpbpwbxzmmtxtxufolxchlealeslcyiweakaoysvijfzmninpmbzeazbjvdyojoyalopdmpdstsymgksuacwsppdmnkiluwoqylyedzzsyhgpxfwyaldfabbstonesihlypcouswkfcywnrggzzkamrtedxyzivuystgiuospvywhqqezjcbnhwzvsoqsbcvccsdhakxcbffrimyiuobwszvccwcdmzknqkicshubettbrvutlhhheuqyjblhvrbabwresreuuzwaeqgaflvcbjmzbenfoekgigcgxawvgnhofkoibvapouamuywgxhivfcchfqiecpltnnebwhgenmnujcrotnrzzrntsrceqaubpcqggoqkzvqnyigbwotnxgehpvcioyevbfqbqodkjsxrkoseytzhhzdymdftgsssibzroetdvhlxsfvqnqwhtyeldmjqdpctdzxkgqkcfmsxanilktehbwcwtaixi", "oqupbcqazvlehlzjyamwlmpybilihvokonzhgqiyomtdxcfcjrvyvzbftvxhcntsavnfumzzozxwpzllomceexaxmablfcluylwwgxzzcrfbusucsdaqlfztvxbwyaygucnowcvvwukhghyzbbwmgvdtcqdvwgulezccmcdmkkftwzodzpnmxxkgmlclgitebyjmferxpnerphcvpvrypnyhvnazizzrmqlpjgkoucmyqdzbwpewgduarfrulybyrokbztghpxojkxespppqpqgnnxacqtzebeogoswbwitciuvqdrlpohhfsgsjhbtgxlegvkovpzdjabojfojubbuabdagjppdtuaevynopbeawkyfevuutdczkxwkkvuiabnkgnscyquirognkzkeeelfmjyljljiozzswkkcxqsajbitjscsnrdzpiuaatkvbfhufaowbdmtydklapdbwlxvxfmoagutecttrbdogxhlrzxbtqqnyzludvwenlrbqehfjkgkcbtnknxcpexgyrkjvfdygoyfzjlceirvhlqrxjgrqxwezwhgnhkrisazhwhzhqdywuorxgmnhbippzuvbarblpbnwznvwnwhmxotwxeadpdcpjelkxopwmizuqctxhoxxrdyaxbvzhrcdtsaaxzehxroqupdigxzdrpbkztvxpnjbnscxvcqxkgfaocyhjqkyxwyogbeoekjepufascoyohlbebqypwvfgvwynfwcpoazzowvbvawvrxovsebibgcuiegpclatcxfiydvpxbolcmwlmwsvryaicjdirggfqykoezcrvzcgcnppdswmxjizjxgvxsitnwbhpfhpvcnliaofdfpwiwylrlaawqljqzpgymhhoygtieqnmujcacvxgzawjvofxsohkmoahshwmgwdarcgbginnrtfekniliwkqxbobcwusprjgasjbppiofeexhgiuxcbhysqpmacufvzjcpbxpdldbvtwpszpwaabqbrhwuczdluybcaelvuhurjwoblkoclsnqpjosgivwiynczedalhpksdibfvuhzcolormvxsbeokfvsbogoubdtzrupvehtdqmewxddjmlnsikxfxudmjqcqhsxlfcxqmgzafpszejwunccnrqmlnuumlxemmrvluioeaqspsvfrbyjjcmlvchjhcvyqzoeqobjeinxdzzwiyinmirkzqndcpmmjpejujfgtcftmccsoarfxvjtdczpvfbgluqvpynqtqmsfpngqeyiimseuldmnjnnwtpuwyggdlybuvpoxfyayhovxzhtlbmsldorjckmywsmigdocgbpbysjrpnxpzafxvbzciasldrtbjsiygspavhalsdvecanlmcmihcmyebtciayyvugavrpcvnjernmaqxusslswgrqauuerjbswsppvsbyffltivkoqkacscyryboknnhbstpmffhvnbznevcmolwvsusmowvybevlyksceaokcnymmgfmmetsacabcsinnqltrxsdnqfseaziyvbecfbacwqimrdgrdwpxrsusmwnervyedswloinjzxfphuvtkvujknlizsxgqoiotniuflvufiftskingufhgvqewvjqbhpyuhgzidoloeibxzwagkpffzotyprkmzajvuahrevwuanmzrqiaoedmdiaghxuslncxunbudftxwipuzihldhcjndwtzqirbwjpqqpckxaweteotuoqtxjsrfzdbwriihvbtnlbtttlnvivfyhetdlvrkqvjqscclmaifqqrgkcegwpzffhfywfaireqazvtkqinfnkzzdhdxdjjnpzyqowacsjhmfrnowekxhnoesupsnatiivxtjphzdonrbvbyrlljyjwyjqkndvskaffacxzcwyfgnpgbrxyqpnwjwvixnjvjykagehbsyxwjvvtlhhxjtqejinhiuejjvnbomyolslaacwcnasyavbcvpiqjldhqenlsmesoauvwekeooaqtlfgtyfgettakefpeknxwmgpxpkkmksfdvrgofgnwgsgadnjwmaltbguxgkajsukrujbrgzpdqxgehheqgniwxvlzdpnmvffxtoiznttsspvrufkkpfhlyenaotplkkfwvojtjnyzitnhnebwthecknkpeevctgtxbbbmmrxdzyeuatgctejpnuljsuoosqhdtpmcbhpmzzbdvhphvurbvurfjbtcoxenxprlodvqgyyooougpnyqqcsauflkbzyatregubqyeemntuilwfbcozptqwszgaueuomxhhrotdqeelblnbmwmhfdbqvtalgfwcxlruqjuxjepurpqkwuxnlajjrfnugtexgdiyxocfeqrmlrrfggbxywbrrmhrablneshhdpxpggkmzfnwdcrkrybzwxngplkvftxjgxfgiuuomvusihtndwmfxialvoujinkwlkydjrmbehskvlulppmdczrzefahwvyakbzjvawxzhqztqswqghubeqhzyuyufiwxmxtyefgxteihyprxbwdykssxadcybtcverkzifjlheqwnpfeckywhusbmqktjhjjsodaqzdsghhaysoilhlqfbgobbwztiouplfeborkkqpqrrcizyazsnmjjyaonwsqcbmmafafsvqofypdxcxsjqufxpxokkqftvneezbpidaqdwiprzztzlhdnyxjzpfplrwksetmdjsoskolwammzedrgwbttgjiznopuuwbqqwlyhrpzrapujnyufljiuwjaanikjsfaohejygudydnlaiczmokjqzkxxdsaexxlddypwgfopyauqvfvawqhxvwwmkiekvkkmojunjzxwiqkigohuwtlqhotzrbhpbvxpczmsqjlhmwbfyzlhlpjeawcxkracgjqmcdmtbzvssvgnuhwroxgoihlgbaxmmakzxxsyvscycylsbaaemmsrifqfcssdhzguueblxomruathvmybhgenytgddikaaogkwssdibperbodtberrnkrdqicgnzwfxaoaqmfovjfetzrvpcsgpeeytxpbtefkwjgmuydmebhxwafemwlncgkwayljaatmmanmpfekwdtmvjqppuknagllcoyixpykxmvykfrfrwmiitxwvzwgiikzwhyhekgsyqivdizzwemotanlmtofjlcilwntqwwumgamtwszhfwcicqeqbxlpaotqfrgbehfcooooteeztiznxevlnkhqhtoerbvuzaxyslvtvelysgashucyvocysscbacshieepypttkkgbyebsrlbyrbsdadnunzzkwbyzspxecoblwmkmtnsatssazxwivfzwifiucrwofdbcaazxdofglusktgrjivedhokzdvdhtreingnglymhujlxrakfesmtetxildrpxazibxxndxctkpvuzwisazhbkitwmbejzhzvafhtaisvjjvzyivmdghrmduheifbvwwjypbcxflesxswzybfayuzklcmjfzvcwuazemnaozqvprubrdzotggqkbwfjbsiyacsqyrnqdthyhemowcbxdapfuoohskvnyjehjzvyrzskjeenfxurfalblwaklfevbgeiniihdcgaskpaqkxakrxwtklffhfvgoetfxuvpjrstdhcuithgsgdtqwuqbwjdjxctttmfrhkliyaylsdowzyrtwenotyfourzhkqidkzmoqfbpwnodcyjnsbksbqymnvuvudsqwfnykavdpnyszbwofjxdjfhihztefusfvjcrgmoehigqsqhhkfcauqjgxzjhinydrbgapdrnzxcljdjzlwfliwhbcvosjviehzpdvxvigvaxtlctrtsctcaizxghlukazxjahjpmhwbcdcqdmvdadsluekbwwhzxrqwopdcecvpryeljmwzjotlapnunnpslbkehepwztlcauadepikdljsunxisiajtiqtdazgtizxmnilfrvhmyojdddxzsuzfychpysdsiczkzctydwuwfkehxnfijhnwvwxaundogctgqcuuqpbewoqhwvgrqslrlvtlqvzuqmllvcpuikqrqdivfcfjvfohzfmvkyqbcahaarcyacidsfdobrbgclxkuijwdaaxpdtjbzudxegdijfecmmobbqeioogpthtdpvuzjqciiyfikvgzbpozxpksgnfgmrfqqcufjulngtaayzrqnhhgcxrjgroqltxwzammhoxfcykalbsutmwptspfcriqbhsxhjjhqyayquztgpsjvxbctfzskvqnsaiprqqtfzlelkgthqfpbwyjxiddryedqejhjrmzadkzdcpcekvuyyvhwqgadsgmdvukdypufnotfutlnnvfntzqzglgbfxtbhzczzfhcyvfidpcpchzsdbzoeodexitmbuksjbyffpxgvptfpqkeccxpjweokjpxvtsutezxyqpbsxekeacpxqbuhjcbrmprgisuuxoxehopkhmaqojxvodzblpiegmjtrhbijhvrogimhdfzoxpnofyujwqqzarheceiiirmuflxhcfjxqmadisviqjfzkmccnydksegmnwfdxxbngudcwthnbhockycjnzolwpxfkljmffqjoljsqcorbciunavkgfubnjamqspijnoabmyjlrtkefaiceufpffvwnygcxwrthyqerjedqyvpwtezyrvvjztrxcxqqywebiqbcmnzuavbnpdyigtsyeojvubqhvetoocfifxqqczmnhmbxcxoxfdmjopxalqrivjkcayonnolylghzkajbxnxzwmnfsszryatbdhlhmoobxkxrwiwuezhujdpvqhohuevcmmjufkbzqriivpxvgvvjyvaipoewijpptjgpzsetuywcnfljssallxikayhjrjyedrlyboracgykaooieegeeubbrzsvuovdprsjifpihmuwwrgjhufsdwwbhhrloolxencdaiwhwrmsaqyamuwmicdzoignydtfnzwrwpbpwbxzmmtxtxufolxchlealeslcyiweakaoysvijfzmninpmbzeazbjvdyojoyalopdmpdstsymgksuacwsppdmnkiluwoqylyedzzsyhgpxfwyaldfabbstonesihlypcouswkfcywnrggzzkamrtedxyzivuystgiuospvywhqqezjcbnhwyvsoqsbcvccadhakxcbffrimyiuobwszvccwcdmzknqkicshubettbrvutlhhheuqyjblhvrbabwresreuuzwaeqgaflvcbjmzbenfoekgigcgxawvgnhofkoikvapouamuywgxhivfcchfqiecpltnnebwhgenrnujcrotnrzzrntsrceqaubpcqggoqkzvqnyigbwotnxgehpvcioyevbfqbqodkjsxrkoseytzhhzdymfftgsssibaroetdvhlxsfvqnqwhtyeldmjqdpctdzxkgqkcfmsxanilktehbwcwtaixiefnhewlzmfeefpldmeptjjshxebbwrbmhrmybddxovkszadbyeqvrxncffozgozdrro", True),
        ]
for s1, s2, expected in data:
    real = s.checkInclusion(s1, s2)
    if 10 < len(s1) and 10 < len(s2):
        print('{}..., {}..., expected {}, real {}, result {}'.format(s1[:10], s2[:10], expected, real, expected == real))
    elif 10 < len(s2):
        print('{}, {}..., expected {}, real {}, result {}'.format(s1, s2[:10], expected, real, expected == real))
    else:
        print('{}, {}..., expected {}, real {}, result {}'.format(s1, s2, expected, real, expected == real))
