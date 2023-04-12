shows=[["NCIS","20x19"],
["The Good Doctor","6x19"],
["All American","5x16"],
["Alaska Daily","1x12"],
["Bobs Burgers","13x01"],
["Rabbit Hole","1x5"],
["Shrinking","1x11"],
["South Park","26x7"],
["Succession","4x4"],
["Ted Lasso","3x5"],
["The Mandalorian","3x7"],
["Will Trent","1x11"]]

quality="1080p"
feed="https://yourfeedhere"
savepath="P:\\\\other.seed"
notfilter="GERMAN|FRENCH|DUBBED"

for showep in shows:
	show=showep[0]
	epfilter=showep[1]
	with open(show+".json", 'w') as f:
		tmp="""{{
    "{0}": {{
       "addPaused": null,
        "affectedFeeds": [
            "{1}"
        ],
        "assignedCategory": "",
        "enabled": true,
        "episodeFilter": "{2}-;",
        "ignoreDays": 1,
        "lastMatch": "",
        "mustContain": "{0} {3}",
        "mustNotContain": "{4}",
        "previouslyMatchedEpisodes": [
        ],
        "savePath": "{5}",
        "smartFilter": true,
        "torrentContentLayout": null,
        "useRegex": null
    }}
}}

"""
		tmp=tmp.format(show,feed,epfilter,quality,notfilter,savepath)
		f.write(tmp)
