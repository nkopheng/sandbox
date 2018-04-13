while read jobName
do
    echo "Current Job Name: ${jobName}"
    echo "java -jar blah.jar"
done < listOfAllJobs.txt
