import {Component, OnInit, signal} from '@angular/core';

declare var QWebChannel: any;

@Component({
  selector: 'app-time-ticker',
  imports: [],
  templateUrl: './time-ticker.html',
  styleUrl: './time-ticker.css'
})
export class TimeTicker implements OnInit {
  bridge: any;
  tick = signal(0);

  ngOnInit() {
    new QWebChannel((window as any).qt.webChannelTransport, (channel: any) => {
      this.bridge = channel.objects.bridge;

      this.bridge.tick.connect((val: number) => {
        console.log('Received from Qt:', val);
        this.tick.set(val);
      });
    });
  }
}
