Highcharts.setOptions({
    chart: {
        style: {
            // fontFamily: "Lato, sans-serif"
        }
    }
});
var month = new Array;
month[0] = "Jan";
month[1] = "Feb";
month[2] = "Mar";
month[3] = "Apr";
month[4] = "May";
month[5] = "Jun";
month[6] = "Jul";
month[7] = "Aug";
month[8] = "Sep";
month[9] = "Oct";
month[10] = "Nov";
month[11] = "Dec";

Highcharts.ajax({
    url: 'assets/trends.json',
    dataType: 'text',
    success: function (activity) {
        activity = JSON.parse(activity);
        var data = []
        console.log(new Date (Date.UTC(2017, 5, 10)))
        activity.forEach(element => {
            
            data.push({
                x: new Date(element['week']),
                y: element['searches']
            })
        });
        var series = {
            type: 'line',
            name: 'Searches',
            data: data,
            color: 'rgb(65,134,244, .8)'
        }
        var albumSeries = {
            name: 'Milestones',
            type: 'scatter',
            data: [
                {
                    name: 'Saturation',
                    day: 'June 9, 2017',
                    x: Date.UTC(2017, 5, 10),
                    y: 0,
                    url: "assets/saturation1.png",
                    color: 'rgb(242,215,117)',
                    desc: "Brockhampton establishes their sound, a unique blend of gangster rap, R&B, experimental production, and charismatic synergy. Each member occupies a niche that compliments the entire group, and the album gains critical acclaim. This boi slaps."
                },
                {
                    name: 'Saturation II',
                    day: 'August 25, 2017',
                    x: Date.UTC(2017, 7, 26),
                    y: 0,
                    url: "assets/saturation2.png",
                    color: 'rgb(242,215,117)',
                    desc: 'Within 2 months, Brockhampton releases a full-length sequel to Saturation, and explodes into the zeitgeist. People are notably surprised that Kevin Abstract, the de facto leader, raps about being gay despite there being very few gay rappers. What an icon.'
                },
                {
                    name: 'Saturation III',
                    day: 'December 15, 2017',
                    x: Date.UTC(2017, 11, 16),
                    y: 0,
                    url: "assets/saturation3.png",
                    color: 'rgb(242,215,117)',
                    desc: 'Saturation III marks the end of a six-month rollout that catapulted Brockhampton to immense success. The cover of all three albums has been Ameer Vann, whose grimy rap style sets the tone for the sonic world that they build. Brockhampton prepares for for what promises to be a very lit tour.'
                },
                {

                    name: 'Brockhampton Separates from Ameer',
                    day: 'May 9, 2018',
                    x: Date.UTC(2018, 4, 10),
                    y: 0,
                    url: "assets/sadbois.png",
                    color: 'rgb(225,45,123)',
                    desc: "In the wave of the #metoo movement, allegations of Ameer's sexual misconduct emerge and are confirmed. Brockhampton removes Ameer from the group and is unable to finish their tour. The album being prepared for release is cancelled, just like Ameer."
                },
                {
                    name: 'Iridescence',
                    day: 'September 21, 2018',
                    x: Date.UTC(2018, 8, 22),
                    y: 0,
                    url: "assets/iridescence.png",
                    color: 'rgb(25,202,26)',
                    desc: "Iridescence is Brockhampton's attempt to sonically and emotionally recoup from Ameer's departure. There are the usual bangers and sadbois and sad bangers, and the absence of Ameer's sound is felt. The other vocalists step up to fill the void left behind."
                },
                {
                    name: 'Ginger',
                    day: 'August 23, 2019',
                    x: Date.UTC(2019, 7, 24),
                    y: 0,
                    url: "assets/ginger.png",
                    color: 'rgb(25,202,26)',
                    desc: "With Ginger, Brockhampton confront their trauma and accept a new path forward. They discuss the ways they decided to cope and grow, and it is rather conclusively the most stylistic change Brockhampton has ever had, with the personal growth they undergo reflected in their new sound."
                },
            ]
        }
        console.log(series)
        Highcharts.chart('timeline', {
            chart: {
            //   backgroundColor: "rgba(255,255,255,.20)",
                backgroundColor:'none',
                height: '40%'
            },
            title: "none",
            // subtitle: {
            //   text: "Timeline of Keanu's Most Notable Films Weighted by Budget and Scored by Rotten Tomatoes"
            // },
            xAxis: {
                offset: 0,
                type: "datetime",
                labels: {
                    step: 1,
                    format: '{value:%Y-%b-%e}'
                  },
                crosshair: true,
                labels: {
                    enabled: true
                }
            }, 
            
            yAxis: {
                gridLineWidth: 0,
                minorGridLineWidth: 0,
                offset: 20,
                min: 0,
                max: 100,
              title: {
                text: '% of Most Searched Month'
              },
              labels: {
                format: '{value}%'
              }
            },
            legend: {
              layout: 'vertical',
              align: 'left',
              verticalAlign: 'top',
              x: 100,
              y: 100,
              floating: true,
              backgroundColor: (Highcharts.theme && Highcharts.theme.legendBackgroundColor) || '#FFFFFF',
              borderWidth: 1,
            },
            plotOptions: {
              scatter: {
                marker: {
                  symbol: 'square',
                  radius: 10,
                  states: {
                    hover: {
                      enabled: true,
                      lineColor: 'rgb(100,100,100)'
                    }
                  }
                },
                states: {
                  hover: {
                    marker: {
                      enabled: false
                    }
                  }
                },
                
              },
              
            },
            tooltip: {
                useHTML: true,
                shared: false,
                
                formatter: function() {
                    console.log(this)
                    url = this.point.url
                    if (url) {
                        var img = `<img style= "padding: 5px; opacity: 0.7;filter: alpha(opacity=100);" height=100 width=100 src ='${url}'>`
                    } else {
                        img = ''
                    }
                    console.log(img)
                    if (this.point.day) {
                        var day = this.point.day + '<br>'
                    } else {
                        var thisDay = new Date(this.point.x)
                        var day = month[thisDay.getMonth()] + ' ' + thisDay.getDay() + ', ' + thisDay.getFullYear() + '<br>'
                    }
                    if (this.point.name) {
                        name = this.point.name + '<br>'
                    } else {
                        name = ''
                    }
                    if (this.point.desc) {
                        desc = this.point.desc + '<br>'
                    } else {
                        desc = ''
                    }
                    return (
                        // '<div><tr><td height=140  style="float:left;">' + img + '</td><td height=140 style="float:right;">' 
                        // + '<b>' + name + day + '</b>'  + desc   
                        //     + '</td>'
                        // + '</tr></div>'
                        '<div style="float:left;">' + img + '</div>' 
                        + '<div style="padding:5px"><b>' + name + day + '</b>'  + desc  + '</div>' 
                    )
                },

            },
            
            series: [albumSeries, series]
          });
          // Add flags for important milestones. This requires Highstock.
    }
})