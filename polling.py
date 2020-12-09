class VotingPoll:
	def __init__(self, csv_file):
		self.csv_file = csv_file
		self.serialized_csv = []
		self._serialize()


	def _serialize(self):
		with open(self.csv_file,'r') as csv:
			lines = csv.readlines()[1:]
			for line in lines:
				self.serialized_csv.append(
					{"candidate":line.split(',')[0], 
					"votes": line.split(',')[1],
					"city": line.split(',')[-1].rstrip()})
		return self.serialized_csv


	def _get_unique_candidates(self):
		uniq_candidate = []
		for vote in self.serialized_csv:
			if not vote['candidate'] == '':
				uniq_candidate.append(vote['candidate'])

		return set(uniq_candidate)

	def _get_unique_cities(self):
		uniq_cities = []
		for vote in self.serialized_csv:
			if not vote['candidate'] == '':
				uniq_cities.append(vote['city'])

		return set(uniq_cities)
		
	def get_votes_per_candidates(self):
		list_of_vote_percandate = []
		for candidate in self._get_unique_candidates():
			count = 0
			for vote in self.serialized_csv:
				if vote['candidate'] == candidate:
					count += int(vote['votes'])
			list_of_vote_percandate.append(
				{"candidate": candidate, 
				"votes_count": count})	
		return list_of_vote_percandate
					
	def get_votes_per_candidates_per_city(self):
		_ = []
		for candidate in self._get_unique_candidates():
			count = 0
			for city in self._get_unique_cities():
				for vote in self.serialized_csv:
					if vote['candidate'] == candidate and vote['city'] == city :
						count += int(vote['votes'])
				_.append({"candidate": candidate, 
				"city": city.rstrip(),
				"votes_count": count})
		return _

	def percentage_vote_per_candidate(self):
		res = []
		total_count = [x['votes_count'] for x in self.get_votes_per_candidates()]
		total_count =sum(total_count)
		for candidate in self.get_votes_per_candidates():

			print("Candidate {} get {}% percent of votes".format(
				candidate['candidate'], 
				candidate['votes_count']*100/total_count))
	


if __name__ == "__main__":
	polling_result = VotingPoll('data.csv')
	polling_result.get_votes_per_candidates()
	polling_result.get_votes_per_candidates_per_city()
	polling_result.percentage_vote_per_candidate()
