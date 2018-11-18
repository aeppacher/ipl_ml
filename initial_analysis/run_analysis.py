import cor_matrix_gen as gen

def main():
    #stats_team
    print "generating coorelation matricies and heatmaps"

    gen.generate("stats_team.csv", "stats_team")
    gen.generate("matches.csv", "matches")
    gen.generate("deliveries.csv", "deliveries")

    print "generation complete"

if __name__ == '__main__':
    main()