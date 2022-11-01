def average_scores(scores_dict: dict):
	if type(scores_dict) == dict:
		scores_sum = 0

		for score in scores_dict:
			scores_sum += scores_dict[score]

		average_score = scores_sum/len(scores_dict)

		return average_score

	else:
		raise TypeError