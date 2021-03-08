from pyspark import SparkContext
sc = SparkContext("local", "BookPairs")

data = sc.textFile("goodreads.user.books1000")
pairs = data.flatmap(lambda line: [(m,s) for m in line.split(":")[1].split(",") for s in line.split(":")[1].split(",") if s<m])
pairs1 = pairs.map(lambda p:(p,1))
pairs0 = pairs1.reduceByKey(lambda a,b:a+b)
pairs0.saveAsTextFile("output")


