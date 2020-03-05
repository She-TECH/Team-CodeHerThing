import { Component } from '@angular/core';
import { ChartsModule } from 'ng2-charts';
import { Label } from 'ng2-charts';
import { ChartType, ChartOptions } from 'chart.js';
import { Router } from "@angular/router";
import { HttpClient } from '@angular/common/http';
import { HttpErrorResponse } from '@angular/common/http';

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


  public pieChartDataOne:any = [
    { 
        data: []
    }];
  

ngOnInit () {
    this.httpService.get('http://localhost:5000/siemens', {responseType: 'json'}).subscribe(
        data => {
          console.log("data");
            this.pieChartDataOne = data as any [];	 // FILL THE CHART ARRAY WITH DATA.
        },
        (err: HttpErrorResponse) => {
            console.log (err.message);
        }
    );
}
 
  // events
  public chartClicked(e:any):void {
    console.log(e);
    this.router.navigate(['/secondPage']);
  }
 
  public chartHovered(e:any):void {
    console.log(e);
  }
  }