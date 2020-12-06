   #Determine winning vote count and candidate.
    #Determine if the votes are greater than the winning count.
    if(votes > winning_count) and (vote_percentage>winning_percentage):
        #If true then set winning_count = votes and winning_percentage = vote_percentage.
        winning_count = votes
        winning_percentage = vote_percentage
        #And, set the winning_candidate equal to the candidate's name.
        winning_candidate = candidate_name