# Cloud-Computing-Redshift
# Abstract (What??): 
An investigation into cloud data storage (Redshift Data warehouse) services for a simulation company.
Redshift basically provides a means for data storage for companies that can be further used for any Business intelligence (BI) related analysis. An analysis is carried out for a sample crash data files provided by the Bureau of Infrastructure, Transport and Regional Economics (BITRE), of the Australian government. A cloud version of data warehouse has been implemented using AWS Redshift and different data warehouse implementations were carried out.
# Why Redshift and this particular implementation (Why??)
Even though there are several traditional data warehousing techniques available, Redshift provides a better way of data storage because of many of its exciting features and advantages over the traditional versions. Apart from that the main reasons I believe motivated me are 

* 1.	System up and running in no time: I was able to design and implement the cloud version (Redshift) data warehouse in less than an hour. (PS: I didn’t have any prior knowledge of cloud computing before the start of this unit). This is ideal for any startup companies or even existing companies to make their data warehouse up and running in less time than compared to a traditional data storage which would take much more than we could ever imagine. 

* 2.	It was easy to implement most of the traditional data warehousing techniques like rollup, drill down, sorting, selection etc with simple SQL queries which improved the performance and is an efficient way of saving time and money.
Apart from this all the advantages of Redshift over traditional data ware house needs to be taken into account as well. 
# How do I Access and Use this (How??)
The AWS Redshift server can be accessed via access Redshift [link!]( https://us-west-2.console.aws.amazon.com/redshift/home?region=us-west-2#cluster-details:cluster=cits5503redshift21679846) , or browse through the AWS console and access the cits5503redshift21679846 cluster. All the SQL queries executed on the server can also be viewed under ‘Query’ tab in the same page. The data provided by BITRE is available [here!] ( http://catalogue.beta.data.wa.gov.au/dataset/crash-2011-to-2015-mrwa ) or can also be accessed through S3 bucket used to for this particular implementation, use this [link!]( https://console.aws.amazon.com/s3/home?region=us-west-2#&bucket=cits5503-21679846-redshift&prefix=CrashData/) to access the S3 bucket where the cleaned data files are stored. 
# Implementation:
As part of implementation, a Redshift cluster and an S3 bucket was created using the AWS console and the BITRE data files were downloaded and kept in the local machine. The data ware house In its core uses a ETL process as part of data cleaning and preprocessing. There were two data files ‘fatalities.csv’ and ‘crashes.csv’. Both these data files were mostly similar but differed only in the case of Age variable included in the fatalities data file which could be used to identify the age of the victim. And the data files has some missing data and unknown columns which needed to be cleaned and a preprocessing of data is essential for the successful BI analysis in future. The data files needed to be free of empty, incorrect and badly formatted values and an ETL process was essential. 
But if I made use of any existing preprocessing tools available on the internet the use of actual coding will be minimal for this (apart from all the sql queries written for analyzing the data). So I decided to use a python program to clean and cleanse the data and sort them out based on the year. The python program was written in such a way that it could be used to clean both files (single program for both data file) and accepts a year as a variable which will handle the data according to the year specified. For eg 
** Python preprocessing.py –f fatalities.csv  2016 **
Will produce the fatalities data set corresponding to only 2016 and 
** Python preprocessing.py –f fatalities.csv  2010-2016 **
Will have data files from 2010 to 2016 and so on. 
 This preprocessed data is then loaded into S3 buckets. Necessary tables are set up in the server and data is copied to database using ‘copy’ command. The advantage of using copy command is that its faster and safer than other means of loading. Proper IAM (access management settings) has to be done in order to copy the data from multiple cloud services. It increases security of data loading and also misuse of data by third parties without proper authorization. The copy command used is

* create table if not exists crashesClean ( Crash_ID varchar,State varchar, Dates varchar,Day Integer, Month varchar,Year integer, Dayweek varchar,TimeOfCrash varchar,Hour integer, Minutes integer,Crash_Type  varchar, Number_of_Fatalities integer,Bus_Involvement varchar, Rigid_Truck_Involvement varchar, Articulated_Truck_Involvement varchar,Speed_Limit integer, count integer);

* create table if not exists fatalitiesClean ( Crash_ID	varchar, State varchar,	Dates varchar,	Day	 integer, Month varchar, Year integer, Dayweek varchar,	TimeofCrash varchar,	Hour integer,	Minutes integer, Crash_Type varchar,	Bus_Involvement varchar, Rigid_Truck_Involvement varchar, Articulated_Truck_Involvement varchar, Speed_Limit varchar,	Road_User varchar,Gender varchar, AgeofVictim integer, count integer);

* copy crashesClean from 's3://cits5503-21679846-redshift/CrashData/crashes_clean.csv' credentials 'aws_iam_role=arn:aws:iam::864718211195:role/CITS5503-Redshift' csv;
* copy fatalitiesClean from 's3://cits5503-21679846-redshift/CrashData/fatalities_clean.csv' credentials 'aws_iam_role=arn:aws:iam::864718211195:role/CITS5503-Redshift' csv;

Redshift automatically identifies and read the data from csv files if specified so. No overhead of changing the format is required and even automatic sorting and distributions can also be done by using proper ‘sortkey’ and ‘distkey’ while creating the table. Advantage of using this distributions and sorting is that with a proper distkey specified, the data is distributed over different nodes based on this key and it improves the efficiency and performance of querying which is analyzed and verified using a different table for both crashes & fatalities data.
Different queries can be run on the server depending upon the analysis to be carried out. Some of the useful analysis and their screen shots are included in the analysis report file attached in the github repository. It has to be noted that this is not limited to what I have implemented and different complex queries can be easily run on the server depending up on the analysis to be carried out. Multiple tables consisting of different values can be stored and “JOIN” using SQL query. There was no need to redistribute the data into multiple tables in my case, hence not implemented that way. But Redshift and sql tools always keep the door open for any types of queries you can run to obtain the desired output, the knowledge of querying is the only barrier to cross. 

# How to run this?How to run this?
This section explains the steps to be followed to install and use redshift and other tools required for data ware house implementation and how to run this on your own computer or on a EC2 virtual machine making the project a total cloud implementation from top to bottom.
* 1.	Create an AWS account and login to the portal using your login credentials.
* 2.	Read the AWS Documentation and follow the links and steps to set up a [S3 bucket] ( http://docs.aws.amazon.com/AmazonS3/latest/dev/UsingBucket.html#create-bucket-intro ) and [Redshift cluster] ( http://docs.aws.amazon.com/redshift/latest/gsg/getting-started.html ). Preferably set up both on the same region, it eases the copy command to be used later in this section. 
* 3.	 After setting up the prerequisites and SQL tools needed to work on Redshift as explained in the step 2, load the workbench and connect it using the secure JDBC url provided while creating the data warehouse.
* 4.	Access the sql server either from your local machine or an EC2 instance depending upon the way you have set up the tools.
* 5.	Down load the BITRE data file from the [link] ( http://catalogue.beta.data.wa.gov.au/dataset/crash-2011-to-2015-mrwa ) provided earlier. 
* 6.	Run the python program and clean the data and save them into your machine.
* 7.	Load the cleaned data onto S3 bucket.
* 8.	Create a table (as explained earlier) in the server space with the distributions and sorting desired. (specify sortkey and distkey . Bear In mind that composite keys can be used in redshift, Ie multiple columns can be treated as sort keys or distributions key.) 
* 9.	Copy the data using the copy command provided in the implementation section. 
* 10.	Run the desired SQL queries and view the out puts either on the workbench or on amazon redshift console. The query tab in Redshift can be accessed through this link.
* 11.	Status, time taken for execution and even the SQL query can be viewed under the query tab. Which indeed is an effective way of logging and rechecking the queries in future if needed.
* 12.	If something goes wrong while executing the queries, the errors can be viewed by using the below query. ( taken from AWS documentation ) 

''' select query, substring(filename,22,25) as filename,line_number as line, 
substring(colname,0,12) as column, type, position as pos, substring(raw_line,0,30) as line_text,
substring(raw_field_value,0,15) as field_text, substring(err_reason,0,45) as reason
from stl_load_errors order by query desc limit 10;
'''
Even a table view can be created to view and manage the errors.  ( AWS Documentation) 

create view loadview as (select distinct tbl, trim(name) as table_name, query, starttime,
trim(filename) as input, line_number, colname, err_code, trim(err_reason) as reason
from stl_load_errors sl, stv_tbl_perm sp where sl.tbl = sp.id);

select table_name, query, line_number, colname, starttime, trim(reason) as error
from loadview where table_name ='crashes' order by line_number limit 1;

* 13.	Use STV_SLICES table to view the current mapping of a slice to a node. ( AWS documentation) 
select  * from stv_slices;

# Functional Requirements: 
* 1.	Data preprocessing using a python program instead of usual ETL tools.
* 2.	The program allows us to clean and create data as required( only for an year or a range of year, which is not the case if uses an existing tool)
* 3.	Various analysis were carried out (BI analysis) which is not actually required for the implementation of Data warehouse. 
* 4.	Compared the time of execution by using distributions and sorting and also in a simple data warehouse design without using both of them.
* 5.	A complete cloud model by using an EC2 instance which uses EC2, Redshift and S3 ( all cloud services)  and cost effective and not time consuming unlike traditional approaches.
* 6.	Far more efficient and easy to implement and analyze when compared to jedox for data mining unit. Overall the time taken for comparing and analyzing were 1/10th of the time required by using Jedox. 

# Non-functional Requirements
* 1.	Easy to implement and use.
* 2.	Cost effective and time efficient with a better performance.
* 3.	Much easier to extend and easy to integrate with all existing ETL and BI tools.
* 4.	Handles huge amount of data without any delay.
* 5.	Easy to view and analyze queries either through the SQL tool or Redshift console.
* 6.	Auto update, upgradation and backups.

# References 
The main resources used for this project includes 
* 1.	AWS documentation for both  [ Redshift ] ( http://docs.aws.amazon.com/redshift/latest/gsg/getting-started.html ) and [ S3 bucket ] ( http://docs.aws.amazon.com/AmazonS3/latest/dev/UsingBucket.html#create-bucket-intro ) creation. 
* 2.	AWS Distribution style documentation 
http://docs.aws.amazon.com/redshift/latest/dg/t_Distributing_data.html
* 3.	Smarter distribution keys and Sort keys available from https://www.periscopedata.com/blog/double-your-redshift-performance-with-the-right-sortkeys-and-distkeys.html
* 4.	SQL query documents: How to group and order in a single query 
http://stackoverflow.com/questions/19698798/oracle-how-to-group-and-order-in-a-single-query
* 5.	Stack overflow : Defining composite keys
http://stackoverflow.com/questions/23575554/redshift-defining-composite-primary-key








