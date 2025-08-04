import {Component, computed, OnInit, signal} from '@angular/core';
import {DatePipe} from '@angular/common';

declare var QWebChannel: any;

@Component({
  selector: 'app-time-ticker',
  imports: [
    DatePipe
  ],
  templateUrl: './time-ticker.html',
  styleUrl: './time-ticker.css'
})
export class TimeTicker implements OnInit {
  ticker: any;
  unixTime = signal(0);

  currentDate = computed(() => {
    const milliseconds = this.unixTime() * 1000;
    return new Date(milliseconds);
  });

  ngOnInit() {
    new QWebChannel((window as any).qt.webChannelTransport, (channel: any) => {
      this.ticker = channel.objects.ticker;

      this.ticker.tick.connect((val: number) => {
        // console.log('Received from Qt:', val);
        this.unixTime.set(val);
      });
    });
  }
}
