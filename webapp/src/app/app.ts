import { Component, signal } from '@angular/core';
import { RouterOutlet, RouterLink } from '@angular/router';
import {routes} from './app.routes';
import {TimeTicker} from './time-ticker/time-ticker';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet, RouterLink, TimeTicker],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {
  protected readonly title = signal('Hybrid App Showcase');
  protected readonly routes = routes;
}
