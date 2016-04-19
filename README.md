# BigDataHomework-MapReduce

Task 1
  - Write a map-reduce job that joins the 'trips' and 'fare' data (taxi data).
  - Note that the 'fares' and 'trips' data share 4 attributes: medallion, hack_license, vendor_id, pickup_datetime.
  - The join MUST BE a reduce-side inner join.
  - Output: A key-value pair per line — use a “tab” to separate the key and the value, a comma between  — where
    
    key: medallion, hack_license, vendor_id, pickup_datetime
    value: remaining attributes of 'trips' data in their original order, and  the remaining attributes of 'fare' data in their original order

    You must respect this ordering!

Here’s a sample output with 2 key-value pairs:
00005007A9F30E289E760362F69E4EAD,2C584442C9DC6740767CDE5672C12379,CMT,2013-08-07 00:55:11    1,N,2013-08-07 00:25:38,1,990,8.9,-73.981972,40.764397,-73.927887,40.865353,CRD,26.5,0.5,0.5,5.5,0,33
00005007A9F30E289E760362F69E4EAD,2C584442C9DC6740767CDE5672C12379,CMT,2013-08-07 02:01:47    1,N,2013-08-07 01:06:05,1,653,3.3,-73.983887,40.780346,-73.991646,40.744511,CSH,12.5,0.5,0.5,0,0,13.5


  - The output directory produced by Hadoop should be named TripFareJoin. Here’s what the contents of the task1 subdirectory should look like:

ls -F task1/
TripFareJoin/    map.py*        reduce.py*

Note: The output directory "TripFareJoin" is not to be included in {netid}_sources.zip. Only include "TripFareJoin" in {netid}_all.zip.

Task 2

Note: Similar to Task 1, you must use a tab to separate the key and the value in the output tuples. 

Write map-reduce jobs for each of the following sub-tasks, using the output of Task 1 (joined data) as input for all these sub-tasks:

    a) Find the distribution of fare amounts (fare_amount) for each of the the following ranges: [0,4], [4.01,8], [8.01,12], [12.01, 16], [16.01, 20], [20.01, 24], [24.01, 28], [28.01, 32], [32.01, 36], [36.01, 40], [40.01, 44], [44.01, 48], [48.01, infinite], i.e., for each range, the number of trips whose fare amount falls in the range.
       Output: A key-value pair per line, where the key is the range, and the value is the number of trips. For example,
       0,4    100
    4.01,8    300
    …
       The output directory produced by Hadoop should be named FareAmounts.
    b) Find the number of trips that cost less than or equal than $10 (total_amount).
       Output: The number of trips.
       The output directory produced by Hadoop should be named TripAmount.

       Note: This task enforces 1 reducer.

    c) Find the distribution of the number of passengers, i.e., for each number of passengers A, the number of trips that had A passengers.
       Output: A key-value pair per line, where the key is the number of passengers, and the value is the number of trips.
       The output directory produced by Hadoop should be named NumberPassengers.
    d) Find the total revenue (for all taxis) and the total amount spent on tolls per day (from pickup_datetime). The revenue should include the fare amount, tips, and surcharges.
       Output: A key-value pair per line, where the key is the day (YYYY-MM-DD), and the value contains the total revenue and the total tolls for that day, in this order.
       The values in the output must have a precision of two decimal digits, e.g., 3.02245 should be represented as 3.02.
    For example,
       2016-01-01    100000.02,11000.00
       2016-01-02    202000.00,1000.00

       The output directory produced by Hadoop should be named TotalRevenue.
    e) For each taxi (medallion) find the total number of trips and the average number of trips per day. For the average trips per day, use 2 decimal digits. 
       Output: A key-value pair per line, where the key is the medallion, and the value contains the total number of trips and the average number of trips per day.
       The output directory produced by Hadoop should be named MedallionTrips.
    f) Find the number of different taxis (medallion) used by each driver (license).
    Output: A key-value pair per line, where the key is the driver, and the value is the number of different taxis used by that driver.
       The output directory produced by Hadoop should be named UniqueTaxis.

===================================================================

Task 3
  - Write a map-reduce job that joins the output from Task 1 with the vehicle data.
  - Note that they both share the medallion attribute.
  - The join MUST BE a reduce-side inner join.
  - Output: A key-value pair per line, where
    
    key: medallion
    value: remaining attributes of Task 1 output (including the remaining keys) in their original order + remaining attributes of vehicle data in their original order

    You should respect this ordering!

  - The output directory produced by Hadoop should be named VehicleJoin.

===================================================================

Task 4
Create map-reduce jobs for the following sub-tasks, using the output from Task 3 as input.
    
Note: In the vehicle data, you may find attributes with commas in the value, so splitting the line by the comma character may not work when reading the attributes (you may end up splitting one attribute in two or more). You can use the csv module (https://docs.python.org/2/library/csv.html) to parse each line; since this module assumes a file as input (not a string), you will need to use StringIO (https://docs.python.org/2/library/stringio.html) as well. Here’s an example:

    csv_file = StringIO.StringIO(line)
    csv_reader = csv.reader(csv_file)
    for record in csv_reader:
        # record is a list containing all the attributes
a) Compare trips based on vehicle_type (WAV, HYB, CNG, LV1, DSE, NRML).
    Output: A key-value pair per line, where the key is the vehicle type, and the value contains the total number of trips, the total revenue, and the average tip percentage (based on the total revenue), in this order.
    All the non-integer values in the output must have a precision of two decimal digits.
The output directory produced by Hadoop should be named VehicleType.
       Note: if total revenue is zero, then tip percentage is zero as well.
    b) List the top 20 agents by total revenue.
       Output: A key-value pair per line, where the key is the agent name, and the value contains the total revenue.
       All the values in the output must have a precision of two decimal digits.
       The output directory produced by Hadoop should be named Top20Revenue.

       Note: This task enforces 1 reducer. (otherwise you may have one Top K for each reducer)
