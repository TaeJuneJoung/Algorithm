data = {
    "movieInfoResult": {
        "movieInfo": {
            "movieCd": "20184574",
            "movieNm": "그린 북",
            "movieNmEn": "Green Book",
            "movieNmOg": "",
            "showTm": "130",
            "prdtYear": "2018",
            "openDt": "20190109",
            "prdtStatNm": "개봉",
            "typeNm": "장편",
            "nations": [
                {
                "nationNm": "미국"
                }
            ],
            "genres": [
                {
                "genreNm": "드라마"
                }
            ],
            "directors": [
                {
                "peopleNm": "피터 패럴리",
                "peopleNmEn": "Peter Farrelly"
                }
            ],
            "actors": [
                {
                "peopleNm": "비고 모텐슨",
                "peopleNmEn": "Viggo Mortensen",
                "cast": "",
                "castEn": ""
                },
                {
                "peopleNm": "마허샬라 알리",
                "peopleNmEn": "Mahershala Ali",
                "cast": "",
                "castEn": ""
                }
            ],
            "showTypes": [
                {
                "showTypeGroupNm": "2D",
                "showTypeNm": "디지털"
                }
            ],
            "companys": [
                {
                "companyCd": "20102327",
                "companyNm": "CGV아트하우스",
                "companyNmEn": "CGV ARTHOUSE",
                "companyPartNm": "배급사"
                },
                {
                "companyCd": "20110854",
                "companyNm": "씨제이이앤엠(주)",
                "companyNmEn": "CJ ENM Corp.",
                "companyPartNm": "수입사"
                }
            ],
            "audits": [
                {
                "auditNo": "2018-MF02280",
                "watchGradeNm": "12세이상관람가"
                }
            ],
            "staffs": [

            ]
        },
        "source": "영화진흥위원회"
    }
}

data_list = data.get("movieInfoResult").get("movieInfo")

movieNm = data_list.get("movieNm")
movieNmEn = data_list.get("movieNmEn")
movieNmOg = data_list.get("movieNmOg")
prdtYear = data_list.get("prdtYear")
genreNm = data_list.get("genres")[0].get("genreNm")
peopleNm = data_list.get("directors")[0].get("peopleNm")
watchGradeNm = data_list.get("audits")[0].get("watchGradeNm")
actors = data_list.get("actors")


for var_i in range(3):
    try:
        globals()[f'actors{var_i+1}'] = actors[var_i].get("peopleNm")
    except IndexError:
        globals()[f'actors{var_i+1}'] = ""

print(movieNm, movieNmEn, movieNmOg, prdtYear, genreNm, peopleNm, watchGradeNm, actors1, actors2, actors3)