import { Component } from '@angular/core';
import { ChartsModule } from 'ng2-charts';
import { Label } from 'ng2-charts';
import { ChartType, ChartOptions } from 'chart.js';
import { Router } from "@angular/router";
import { HttpClient } from '@angular/common/http';
import { HttpErrorResponse } from '@angular/common/http';
import {CompanyData} from '../companydata';

@Component({
    selector: 'first-page',
    templateUrl: './first-page.component.html',
    styleUrls: ['./first-page.component.css']
  })

  export class FirstPageComponent {

    constructor(private router: Router, private httpService: HttpClient){
    }

  public pieChartLabels:string[] = ['New', 'Technology', 'Customer Satisfaction'];
  public pieChartData:number[] = [50, 20, 30];
  public pieChartType:string = 'pie';
  public pieChartDataSiemens:number[] = [];
  public pieChartDataRockwell:number[] = [];
  public pieChartDataAbb:number[] = [];
  public pieChartDataSchinder:number[] = [];
  public pieChartColor:any = [
    {
        backgroundColor: ['rgba(30, 169, 224, 0.8)',
        'rgba(255,165,0,0.9)',
        'rgba(139, 136, 136, 0.9)'
    ]
    }]


  
  

ngOnInit () {
    this.httpService.get('http://localhost:5000/siemens', {responseType: 'json'}).subscribe(
        data => {
          console.log("data");
          let pieData = <CompanyData>data;        
            this.pieChartDataSiemens.push(pieData.new);
            this.pieChartDataSiemens.push(pieData.technology);
            this.pieChartDataSiemens.push(pieData.marketTrend);// FILL THE CHART ARRAY WITH DATA.
        },
        (err: HttpErrorResponse) => {
            console.log (err.message);
        }
    );

    this.httpService.get('http://localhost:5000/abb', {responseType: 'json'}).subscribe(
        data => {
          console.log("data");
          let pieData = <CompanyData>data;        
            this.pieChartDataAbb.push(pieData.new);
            this.pieChartDataAbb.push(pieData.technology);
            this.pieChartDataAbb.push(pieData.marketTrend);// FILL THE CHART ARRAY WITH DATA.
        },
        (err: HttpErrorResponse) => {
            console.log (err.message);
        }
    );

    this.httpService.get('http://localhost:5000/schinder', {responseType: 'json'}).subscribe(
        data => {
          console.log("data");
          let pieData = <CompanyData>data;        
            this.pieChartDataSchinder.push(pieData.new);
            this.pieChartDataSchinder.push(pieData.technology);
            this.pieChartDataSchinder.push(pieData.marketTrend);// FILL THE CHART ARRAY WITH DATA.
        },
        (err: HttpErrorResponse) => {
            console.log (err.message);
        }
    );

    this.httpService.get('http://localhost:5000/rockwell', {responseType: 'json'}).subscribe(
        data => {
          console.log("data");
          let pieData = <CompanyData>data;        
            this.pieChartDataRockwell.push(pieData.new);
            this.pieChartDataRockwell.push(pieData.technology);
            this.pieChartDataRockwell.push(pieData.marketTrend);// FILL THE CHART ARRAY WITH DATA.
        },
        (err: HttpErrorResponse) => {
            console.log (err.message);
        }
    );
}
 
  // events
  public chartClicked(e:any, chartvalue:string):void {
   // console.log(e);
    console.log(chartvalue);
    this.router.navigate(['/secondPage', {company: chartvalue}]);
  }
 
  public chartHovered(e:any):void {
    console.log(e);
  }
  }