
library("dplyr")

TMDB5000_movies <- read.csv("tmdb_5000_movies.csv")

tmp <- tbl_df(TMDB5000_movies)


head(TMDB5000_movies)


TMDB5000_movies %>%
  group_by(release_date) %>%

# ....

