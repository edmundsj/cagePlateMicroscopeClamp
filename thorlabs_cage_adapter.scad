$fa=0.5;
$fs=0.5;
difference(){
    cube(size=[57.2, 17, 42.4]);
    translate(v=[-0.01, -0.005, 1.8]){
        cube(size=[6.51, 17.01, 40.61]);
    };
    translate(v=[50.71, -0.005, 1.8]){
        cube(size=[6.51, 17.01, 40.61]);
    };
    translate(v=[8.3, -0.005, -0.01]){
        cube(size=[40.6, 17.01, 39.61]);
    };
    translate(v=[8.3, 4.05, 0]){
        cube(size=[40.6, 8.9, 40.6]);
    };
    translate(v=[3.1000000000000014, 2.5, -0.005]){
        cylinder(h=1.81, d=3.6);
    };
    translate(v=[54.1, 2.5, -0.005]){
        cylinder(h=1.81, d=3.6);
    };
    translate(v=[3.1000000000000014, 14.5, -0.005]){
        cylinder(h=1.81, d=3.6);
    };
    translate(v=[54.1, 14.5, -0.005]){
        cylinder(h=1.81, d=3.6);
    };
};
