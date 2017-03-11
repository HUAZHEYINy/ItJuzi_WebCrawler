# ItJuzi_WebCrawler
Repository of Web Crawler Project - The data is crawled start from Oct 2016 to Jan 2017.


<H1>OverView</H1>

I am extremly interested in the start up companies. So that, I implemented a web crawler that can crawler the start up companies info
and also some critical information including pre-IPO status and so on. Furthermore, I used several tools to virtualize these info that
we can extract some new info through the chart or graph from it.

<br>
This project is a web crawler project based on Scrapy Framework. 
Using MySQL Database to store the crawled data and also using three data virtualization tools to virtualize part of information.

</br>
Language: Python - 2.7</br>
DB: MySQL</br>
Virtualization Tools: D3.js - javascript; Plotly - Python; Tagexdo.

</br>Target Website: https://www.itjuzi.com/special/chollima/

<h2>LitttleDetails</h2>
The picture below is showing the most common location of start up company which has high value of assessment. 
basically, the bigger city name is, the more company are in the city.
<img src="https://github.com/HUAZHEYINy/ItJuzi_WebCrawler/blob/master/it_juzi/Result/Image/16MP_城市.png" alt="City">
Pie Chart showing the percentage.
<img src="https://github.com/HUAZHEYINy/ItJuzi_WebCrawler/blob/master/it_juzi/Result/Image/ScopePercentage.png" alt="CityPieChart">
<br>
The picture below is showing the different industries where start up company have high value of assessment.  
basically, the bigger industry name is, the more comany are in the industry.
<img src="https://github.com/HUAZHEYINy/ItJuzi_WebCrawler/blob/master/it_juzi/Result/Image/16MP_行业.png" alt="Industry">
<br>
The picture below is showing the ranking of invest firm based on the number of company which they are invested. 
<img src="https://github.com/HUAZHEYINy/ItJuzi_WebCrawler/blob/master/it_juzi/Result/Image/Invest_Firm.png" alt="InvestFirm">
<br>

I pulled all of the data which include everything about the company from database, Since it is too big and will slow down the trffic,
If u want to see it. Pleas click below.
<br>
<a href="https://github.com/HUAZHEYINy/ItJuzi_WebCrawler/blob/master/it_juzi/Result/Image/final_data.pdf">See the details of result data</a>

