import cor_matrix_gen as gen

def main():
    #stats_team
    print "generating coorelation matricies and heatmaps"

    gen.generate("indices_match.csv", "indices_match")
    gen.generate("indices_team.csv", "indices_team")
    gen.generate("overall_indices.csv", "overall_indices")
    gen.generate("stats_team.csv", "stats_team")

    print "generation complete"

if __name__ == '__main__':
    main()