import { Routes } from '@angular/router';
import {Hello} from './hello/hello/hello';
import {Top} from './top/top/top';

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
];
