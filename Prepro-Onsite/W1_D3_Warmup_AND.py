""" W1_D3_Warmup_AND """
def main(inputa):
    """
    Omoi dashiteita no wa mata, kazoku no koto
    Ayano wa onechan dakara minna no koto, yoroshiku ne

    Aka renga no kabe chisana ie no naka de
    Hisohiso hanasou himitsu no sakusen mitai ni
    Tsurete korareta sannin no makka na me ni wa
    Otona ni kakushiteita kako ga aru

    Obieta kao de Boku wa bakemono dakara
    Watashi wa tsugeru Sonna koto wa nai yo tte
    Makka no iro wa shujinko no iro dakara, obietainakute mo, yoi nda yo

    Omoshiroi koto nayande wa
    Kyou mo onechan butte
    Hora, mite ite
    Akai mafura makitsuketa
    Himitsu soshiki mitai!

    Akane iro, somete, hajimeyou
    Chisana hīrō no furi dakedo
    Sukoshi demo, mata waraetara tte
    Kyou mo kazoku de iyou
    Shiawase o negaou, saki ni aru mirai ga
    Dore dake kanashikute mo
    Kono koto wa himitsu dayo
    Tanoshikute yō ga shizunda

    Harukaze meguri otona ni natta sekai wa
    Rifujin ni magaru dareka no inbo mitai ni
    Fukurande kieta aisuru hito no namida wa
    Dare mo kidzukenakute, kurokunaru

    Kurui dashiteita kidzuitara mo
    Darenimo ienakute
    Yada, yadayo. Kowareru no wa
    Shiawaseno owaru sekai ga kuru
    Akaneiro, onegai. Kore ijou,
    Dareka no mirai o kowasanaide
    Nakinagara mata, kangaeru
    Egao ni kakushita mama
    Akame iro, sore ga watashinara
    Dareka no mirai o sukueru kana
    Bukiyou de, nasakenai
    Hitoribocchi no sakusenda
    Watashi ga kieta ano hi no himitsu soshiki wa
    Chanto waratte kurasete iru no kana
    Kitto, watashi wa okorare chau na
    Dakedo, chanto onechan ni nareta kana

    Omoi dashite miyou
    Ano sukidatta kotoba
    Shiawase" tte nandaka fushigi
    Ashita no koto, suki ni nareru
    """

    if inputa != "True":
        ["Error", "False"][inputa == "False"]
    else:
        inputb = input()
        if (inputa == "True" or inputa == "False") and (inputb == "True" or inputb == "False"):
            print(["False", "True"][inputa == "True" and inputb == "True"])
        else:
            print("Error")
main(input())
