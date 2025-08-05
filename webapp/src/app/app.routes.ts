import { Routes } from '@angular/router';
import {Hello} from './hello/hello';
import {Top} from './top/top';
import {TimeTicker} from './time-ticker/time-ticker';

export const routes: Routes = [
  {
    path: '',
    component: Top,
    title: 'Top'
  },
  {
    path: 'hello',
    component: Hello,
    title: 'Hello'
  },
  {
    path: 'time-ticker',
    component: TimeTicker,
    title: 'Time Ticker'
  },
];
