import { Component } from '@angular/core';
import { ChartsModule } from 'ng2-charts';
import { Label } from 'ng2-charts';
import { ChartType, ChartOptions } from 'chart.js';
import { Router } from "@angular/router";
//import * as pluginDataLabels from 'chartjs-plugin-datalabels';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {

  constructor(private router: Router){
  }

  title = 'frontend';

 // public pieChartLabels:string[] = ['New', 'Technology', 'Customer Satisfaction'];
 // public pieChartData:number[] = [50, 20, 30];
//  public pieChartType:string = 'pie';
 
  // events
 // public chartClicked(e:any):void {
 //   console.log(e);
   // this.router.navigate(['/secondPage']);
 // }
 
 // public chartHovered(e:any):void {
 //   console.log(e);
 // }

  home() {
    //alert("Welcome");
    this.router.navigate(['/']);
  }

  refresh(){
    alert("refresh");
  }
}
