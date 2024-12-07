# Pulse-width Modulation Driver

![pwm_driver_pcb_image](https://github.com/mjkloeckner/driver_PWM/assets/64109770/73f584bb-5474-498c-a39f-cb8020b2aa48)

This is a simple [Pulse-width Modulation](https://en.wikipedia.org/wiki/Pulse-width_modulation) Driver that
can drive LED strips or other DC loads. The base schematic is taken from
[Creastive Creator's post](https://www.hackster.io/dhritimanhb2015/led-dimmer-circuit-with-555-timer-bc30f7) on [hackster.io](https://hackster.io).

## 3D Models used on the PCB

The majority of 3D Models used are from the official KiCAD 3D library. The ones
missing, which the KiCAD 3D library does not include are designed from scratch
using FreeCAD (located on `pwm_driver_kicad/pwm_driver_3d_models`). There's also
thrid-party 3D models which have much more detail, for example:

- [16mm Alpha Potentiometer](https://grabcad.com/library/alpha-rv16af-20-1)
- [Screw terminal DG-301 5mm](https://grabcad.com/library/screw-terminal-dg-301-5mm-1)

## Case

The case for the projects has been developed using FreeCAD.

### Considerations

- Fully parametric design: The majority of the values used in the design can be
  easily changed by modifying the contents of the `param` spreadsheet
- No threaded holes: Even tho FreeCAD offers an option to thread the holes,
  considering that the screws used have a diameter that is less than `3.5 mm`
  and the majority of 3D printers don't have that level of detail, I considered
  not doing the thread on holes and doing it later with the physical screw at
  the time of the build.

## Resources Consulted

This are some web resources that I consulted during the build

- [Electronics enclosure for 3D printing // FreeCAD + KiCAD complete
  walkthrough](https://www.youtube.com/watch?v=ov3PpaP9uHI)

## License

[MIT](https://opensource.org/licenses/MIT)
