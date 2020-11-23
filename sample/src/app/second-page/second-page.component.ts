import { Component, OnInit } from '@angular/core';
import { Router } from "@angular/router";
import { HttpClient } from '@angular/common/http';
import { HttpErrorResponse } from '@angular/common/http';
import { ActivatedRoute } from "@angular/router";
import {DetailData} from '../newdata'
import {UrlData} from '../urlData';
import { AllNewsData } from '../allNewsData';

@Component({
  selector: 'app-second-page',
  templateUrl: './second-page.component.html',
  styleUrls: ['./second-page.component.css']
})
export class SecondPageComponent implements OnInit {

  public pieChartLabels1:string[] = ['Renewable', 'Energy Automation', 'O&G', 'Process Automation'];
  public pieChartLabels2:string[] = ['CyberSecurity', 'DigitalTwin', 'AI', 'IoT','Blockchain', 'Robotics', 'Hardware'];
  public pieChartLabels3:string[] = ['New Release', 'Collaboration'];
  public pieChartDataDomain:number[] = [];
  public pieChartDataTech:number[] = [];
  public pieChartDataMarket:number[] = [];
  public firstChart = true;
  public pieChartColor:any = [
    {
        backgroundColor: ['rgba(30, 169, 224, 0.8)',
        'rgba(255,165,0,0.9)',
        'rgba(153,0,76, 0.9)',
        'rgba(120, 167, 100, 0.9)',
        'rgba(25,0,51, 0.9)',
        'rgba(0,153,153, 0.9)',
        'rgba(204,0,0, 0.9)'
    ]
    }]
  public pieChartType:string = 'pie';
  public secChart = false;
  public thirdChart = false;
  public chartValue:string;
  public allChartDataList:UrlData;
  allData: AllNewsData[]

  constructor(private router: Router, private route: ActivatedRoute,private httpService: HttpClient){
    this.chartValue = route.snapshot.params['company']
    console.log(this.chartValue)
    this.allChartDataList = new UrlData();
    this.allChartDataList.news = []
  }

  ngOnInit () {
  
  
    
    console.log(this.chartValue)
    if (this.chartValue == 'Siemens')
    {
        this.httpService.get('http://localhost:5000/siemensdetails', {responseType: 'json'}).subscribe(
        data => {
          console.log(data);
          let pieData = <DetailData>data;        
            this.pieChartDataDomain.push(pieData.di);
            this.pieChartDataDomain.push(pieData.si);
            this.pieChartDataDomain.push(pieData.mo);
            this.pieChartDataDomain.push(pieData.energy);
            

            this.pieChartDataTech.push(pieData.cs);
            this.pieChartDataTech.push(pieData.dt);
            this.pieChartDataTech.push(pieData.da);
            this.pieChartDataTech.push(pieData.ce);
            this.pieChartDataTech.push(pieData.block);
            this.pieChartDataTech.push(pieData.robot);
            this.pieChartDataTech.push(pieData.add);

            this.pieChartDataMarket.push(pieData.sec);
            this.pieChartDataMarket.push(pieData.coll);


            
        },
        (err: HttpErrorResponse) => {
            console.log (err.message);
        }
    );

    this.httpService.get('http://localhost:5000/siemensallnews', {responseType: 'json'}).subscribe(
      data => {
        this.allData = <AllNewsData[]>data
        for (let i = this.allData.length - 1; i >= 0; i--) {
          this.allChartDataList.news.push(this.allData[i]);
        }
        })  
    

    }

    if (this.chartValue == 'ABB')
    {
        this.httpService.get('http://localhost:5000/abbdetails', {responseType: 'json'}).subscribe(
        data => {
          console.log(data);
          let pieData = <DetailData>data;        
            this.pieChartDataDomain.push(pieData.di);
            this.pieChartDataDomain.push(pieData.si);
            this.pieChartDataDomain.push(pieData.mo);
            this.pieChartDataDomain.push(pieData.energy);
           
            this.pieChartDataTech.push(pieData.cs);
            this.pieChartDataTech.push(pieData.dt);
            this.pieChartDataTech.push(pieData.da);
            this.pieChartDataTech.push(pieData.ce);
            this.pieChartDataTech.push(pieData.block);
            this.pieChartDataTech.push(pieData.robot);
            this.pieChartDataTech.push(pieData.add);

            this.pieChartDataMarket.push(pieData.sec);
            this.pieChartDataMarket.push(pieData.coll);


            
        },
        (err: HttpErrorResponse) => {
            console.log (err.message);
        }
    );
    this.httpService.get('http://localhost:5000/abballnews', {responseType: 'json'}).subscribe(
      data => {
        this.allData = <AllNewsData[]>data
        for (let i = this.allData.length - 1; i >= 0; i--) {
          this.allChartDataList.news.push(this.allData[i]);
        }
        })
      }

    if (this.chartValue == 'Honeywell')
    {
        this.httpService.get('http://localhost:5000/rockwelldetails', {responseType: 'json'}).subscribe(
        data => {
          console.log(data);
          let pieData = <DetailData>data;        
            this.pieChartDataDomain.push(pieData.di);
            this.pieChartDataDomain.push(pieData.si);
            this.pieChartDataDomain.push(pieData.mo);
            this.pieChartDataDomain.push(pieData.energy);
           
            this.pieChartDataTech.push(pieData.cs);
            this.pieChartDataTech.push(pieData.dt);
            this.pieChartDataTech.push(pieData.da);
            this.pieChartDataTech.push(pieData.ce);
            this.pieChartDataTech.push(pieData.block);
            this.pieChartDataTech.push(pieData.robot);
            this.pieChartDataTech.push(pieData.add);
           

            this.pieChartDataMarket.push(pieData.sec);
            this.pieChartDataMarket.push(pieData.coll);


            
        },
        (err: HttpErrorResponse) => {
            console.log (err.message);
        }
    );
    this.httpService.get('http://localhost:5000/rockwellallnews', {responseType: 'json'}).subscribe(
      data => {
        this.allData = <AllNewsData[]>data
        for (let i = this.allData.length - 1; i >= 0; i--) {
          this.allChartDataList.news.push(this.allData[i]);
        }
        })
    
    }

    if (this.chartValue == 'Emerson')
    {
        this.httpService.get('http://localhost:5000/schinderdetails', {responseType: 'json'}).subscribe(
        data => {
          console.log(data);
          let pieData = <DetailData>data;        
            this.pieChartDataDomain.push(pieData.di);
            this.pieChartDataDomain.push(pieData.si);
            this.pieChartDataDomain.push(pieData.mo);
            this.pieChartDataDomain.push(pieData.energy);
          
            this.pieChartDataTech.push(pieData.cs);
            this.pieChartDataTech.push(pieData.dt);
            this.pieChartDataTech.push(pieData.da);
            this.pieChartDataTech.push(pieData.ce);
            this.pieChartDataTech.push(pieData.block);
            this.pieChartDataTech.push(pieData.robot);
            this.pieChartDataTech.push(pieData.add);

            this.pieChartDataMarket.push(pieData.sec);
            this.pieChartDataMarket.push(pieData.coll);


            
        },
        (err: HttpErrorResponse) => {
            console.log (err.message);
        }
    );

    this.httpService.get('http://localhost:5000/schniderallnews', {responseType: 'json'}).subscribe(
      data => {
        this.allData = <AllNewsData[]>data
        for (let i = this.allData.length - 1; i >= 0; i--) {
          this.allChartDataList.news.push(this.allData[i]);
        }
        })
  }


}

}
