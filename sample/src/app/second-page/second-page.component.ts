import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-second-page',
  templateUrl: './second-page.component.html',
  styleUrls: ['./second-page.component.css']
})
export class SecondPageComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
  }

  public pieChartLabels1:string[] = ['DI', 'SI', 'MO', 'Energy'];
  public pieChartLabels2:string[] = ['CS', 'DT', 'DA', 'CED','Blockchanin', 'AR', 'AM'];
  public pieChartLabels3:string[] = ['New', 'Technology', 'Customer Satisfaction'];
  public pieChartData:number[] = [50, 20, 30];
  public pieChartType:string = 'pie';
  public firstChart = false;
  public secChart = false;
  public thirdChart = false;

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
