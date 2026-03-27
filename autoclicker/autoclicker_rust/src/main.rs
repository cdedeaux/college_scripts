use fltk::{app, button::Button, frame::Frame, prelude::*, window::Window};

fn main(){
    let app = app::App::default();
    let mut wind = Window::new(100, 100, 400, 300, "Cool autclicker");
    let mut frame = Frame::new(0, 0, 400, 200, "");
    let mut but = Button::new(160, 210, 80, 40, "Click me!");
    wind.end();
    wind.show();
    app.run().unwrap();
    let clicking: bool = false;

}