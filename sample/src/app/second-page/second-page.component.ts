import { Component, OnInit } from '@angular/core';
import { Router } from "@angular/router";
import { HttpClient } from '@angular/common/http';
import { HttpErrorResponse } from '@angular/common/http';
import { ActivatedRoute } from "@angular/router";
import {DetailData} from '../newdata'

@Component({
  selector: 'app-second-page',
  templateUrl: './second-page.component.html',
  styleUrls: ['./second-page.component.css']
})
export class SecondPageComponent implements OnInit {

  public pieChartLabels1:string[] = ['DI', 'SI', 'MO', 'Energy', 'Healthcare'];
  public pieChartLabels2:string[] = ['CS', 'DT', 'DA', 'CED','Blockchain', 'AR', 'AM'];
  public pieChartLabels3:string[] = ['Security', 'Collaboration'];
  public pieChartDataDomain:number[] = [];
  public pieChartDataTech:number[] = [];
  public pieChartDataMarket:number[] = [];
  public pieChartColor:any = [
    {
        backgroundColor: ['rgba(30, 169, 224, 0.8)',
        'rgba(255,165,0,0.9)',
        'rgba(139, 136, 136, 0.9)',
        'rgba(139, 136, 100, 0.9)',
        'rgba(139, 136, 120, 0.9)',
        'rgba(139, 136, 130, 0.9)',
        'rgba(139, 136, 140, 0.9)'
    ]
    }]
  public pieChartType:string = 'pie';
  public firstChart = false;
  public secChart = false;
  public thirdChart = false;
  public chartValue:string;

  constructor(private router: Router, private route: ActivatedRoute,private httpService: HttpClient){
    this.chartValue = route.snapshot.params['company']
    console.log(this.chartValue)
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
            this.pieChartDataDomain.push(pieData.health);

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
            this.pieChartDataDomain.push(pieData.health);

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
    }

    if (this.chartValue == 'Rockwell')
    {
        this.httpService.get('http://localhost:5000/rockwelldetails', {responseType: 'json'}).subscribe(
        data => {
          console.log(data);
          let pieData = <DetailData>data;        
            this.pieChartDataDomain.push(pieData.di);
            this.pieChartDataDomain.push(pieData.si);
            this.pieChartDataDomain.push(pieData.mo);
            this.pieChartDataDomain.push(pieData.energy);
            this.pieChartDataDomain.push(pieData.health);

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
    }

    if (this.chartValue == 'Schneider')
    {
        this.httpService.get('http://localhost:5000/schinderdetails', {responseType: 'json'}).subscribe(
        data => {
          console.log(data);
          let pieData = <DetailData>data;        
            this.pieChartDataDomain.push(pieData.di);
            this.pieChartDataDomain.push(pieData.si);
            this.pieChartDataDomain.push(pieData.mo);
            this.pieChartDataDomain.push(pieData.energy);
            this.pieChartDataDomain.push(pieData.health);

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
    }
  
/*
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
    );*/
}
 

  

  // events
  public chartClicked1(e:any):void {
    console.log("clicked");
    console.log(e);
    e = true;
    this.firstChart = true;
    this.secChart = false;
    this.thirdChart = false;
    console.log(e);
  }


  public chartClicked2(e:any):void {
    console.log("clicked====");
    this.secChart = true;
    this.firstChart = false;
    this.thirdChart = false;
  }

  public chartClicked3(e:any):void {
    console.log("clicked====");
    this.thirdChart = true;
    this.firstChart = false;
    this.secChart = false;
  }
 
  public chartHovered(e:any):void {
    console.log(e);
  }
 

}
