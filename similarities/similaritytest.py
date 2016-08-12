from similaritymodule import Similarity

def main():
	measure = Similarity()

	print measure.jaccard_similarity([1,1],[1,1])
	print measure.euclidean_distance([1,1],[2,2])


if __name__ == "__main__":
	main()


