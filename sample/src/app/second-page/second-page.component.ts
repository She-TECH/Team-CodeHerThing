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

  public pieChartLabels:string[] = ['A', 'B', 'C'];
  public pieChartData:number[] = [50, 20, 30];
  public pieChartType:string = 'pie';

  // events
  public chartClicked(e:any):void {
    console.log("clicked");
    
  }
 
  public chartHovered(e:any):void {
    console.log(e);
  }
 

}
