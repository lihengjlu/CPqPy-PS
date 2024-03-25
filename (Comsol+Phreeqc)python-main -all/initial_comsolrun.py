# ------------------------------初始化comsol-----------



inputcomsolstr0 = """

function out = model
%
% test1.m
%
% Model exported on Jan 24 2022, 11:20 by COMSOL 5.6.0.280.

import com.comsol.model.*
import com.comsol.model.util.*

model = ModelUtil.create('Model');

model.modelPath('I:\Desktop');

model.component.create('comp1', true);

model.component('comp1').geom.create('geom1', 2);

model.component('comp1').mesh.create('mesh1');

model.component('comp1').physics.create('spf', 'LaminarFlow', 'geom1');
model.component('comp1').physics.create('tds', 'DilutedSpecies', {'c'});

model.param().set("U_mean", "0.00012[m/s]", "Mean inflow velocity");
model.param().set("L", "0.0005[m]", "Height");
model.param().set("W", "0.001[m]", "Width");
model.param().set("R", "0.0001[m]", "Cylinder radius");
model.param().set("SI", "0", "Saturation index");

model.component('comp1').geom('geom1').lengthUnit('cm');
model.component("comp1").geom("geom1").create("imp1", "Import");
model.component("comp1").geom("geom1").feature("imp1").set("filename", "D:\\2DFlow\\Untitled.mphbin");
model.component('comp1').geom('geom1').run;

model.component('comp1').common.create('free1', 'DeformingDomainDeformedGeometry');
model.component('comp1').common('free1').selection.all;
model.component('comp1').common('free1').selection.set([1]);
model.component('comp1').common('free1').set('smoothingType', 'laplace');
model.component('comp1').common.create('pnmv1', 'PrescribedNormalMeshVelocityDeformedGeometry');
model.component('comp1').common('pnmv1').selection.set([5 6 7 8]);
model.component('comp1').common('pnmv1').set('prescribedNormalVelocity', '0.0000369*(1.55038E-06+5.01467E-04*H)*(1-10^(SI))');



model.component('comp1').material.create('mat1', 'Common');
model.component('comp1').material('mat1').propertyGroup('def').set('density', {'1'});
model.component('comp1').material('mat1').propertyGroup('def').set('dynamicviscosity', {'3e-3'});

model.component('comp1').physics('spf').create('inl1', 'InletBoundary', 1);
model.component('comp1').physics('spf').create('out1', 'OutletBoundary', 1);
model.component('comp1').physics('spf').feature('inl1').selection.set([1]);
model.component('comp1').physics('spf').feature('out1').selection.set([4]);

model.component("comp1").physics("spf").feature("inl1").set("ComponentWise", "VelocityFieldComponentWise");
model.component("comp1").physics("spf").feature("inl1").set('u0', {'0.00012' '0' '0'});
model.component("comp1").physics("spf").feature("inl1").set("BoundaryCondition", "Velocity");


model.component('comp1').physics('tds').feature('cdm1').set('u_src', 'root.comp1.u');
model.component("comp1").physics("tds").field("concentration").component(1, "H");
model.component("comp1").physics("tds").field("concentration").component(2, "Ca");
model.component("comp1").physics("tds").field("concentration").component(3, "C");
model.component("comp1").physics("tds").field("concentration").component(4, "Al");
model.component("comp1").physics("tds").field("concentration").component(5, "Na");
model.component("comp1").physics("tds").field("concentration").component(6, "K");
model.component("comp1").physics("tds").field("concentration").component(7, "Fe");
model.component("comp1").physics("tds").field("concentration").component(8, "Mg");
model.component("comp1").physics("tds").field("concentration").component(9, "SO4");
model.component("comp1").physics("tds").field("concentration").component(10, "Si");
model.component("comp1").physics("tds").field("concentration").component(11, "Cl");
model.component("comp1").physics("tds").feature("init1").setIndex("initc", 950, 2);
model.component("comp1").physics("tds").feature("init1").setIndex("initc", 28.7, 1);
model.component("comp1").physics("tds").feature("init1").setIndex("initc", 0.0174, 3);
model.component("comp1").physics("tds").feature("init1").setIndex("initc", 489, 4);
model.component("comp1").physics("tds").feature("init1").setIndex("initc", 0.0213, 5);
model.component("comp1").physics("tds").feature("init1").setIndex("initc", 0.0733, 6);
model.component("comp1").physics("tds").feature("init1").setIndex("initc", 0.00452, 7);
model.component("comp1").physics("tds").feature("init1").setIndex("initc", 2.04E-4, 8);
model.component("comp1").physics("tds").feature("init1").setIndex("initc", 0.544, 9);
model.component("comp1").physics("tds").feature("init1").setIndex("initc", "0.316", 0);
model.component("comp1").physics("tds").feature("init1").setIndex("initc", "516", 10);
model.component('comp1').physics('tds').create('out1', 'Outflow', 1);
model.component('comp1').physics('tds').feature('out1').selection.set([4]);
model.component('comp1').physics('tds').create('in1', 'Inflow', 1);
model.component("comp1").physics("tds").feature("in1").selection().set(1);
model.component("comp1").physics("tds").feature("in1").setIndex("c0", 28.7, 1);
model.component("comp1").physics("tds").feature("in1").setIndex("c0", 0.0174, 3);
model.component("comp1").physics("tds").feature("in1").setIndex("c0", 489, 4);
model.component("comp1").physics("tds").feature("in1").setIndex("c0", 0.0213, 5);
model.component("comp1").physics("tds").feature("in1").setIndex("c0", 0.0733, 6);
model.component("comp1").physics("tds").feature("in1").setIndex("c0", 0.00452, 7);
model.component("comp1").physics("tds").feature("in1").setIndex("c0", 2.04E-4, 8);
model.component("comp1").physics("tds").feature("in1").setIndex("c0", 0.544, 9);
model.component("comp1").physics("tds").feature("in1").set("BoundaryConditionType", "ConcentrationConstraint");
model.component("comp1").physics("tds").feature("in1").setIndex("c0", 0.316, 0);
model.component("comp1").physics("tds").feature("in1").setIndex("c0", 516, 10);
model.component("comp1").physics("tds").feature("in1").setIndex("c0", 950, 2);

model.component('comp1').physics('tds').create('fl1', 'FluxBoundary', 1);
model.component('comp1').physics('tds').feature('fl1').selection.set([5 6 7 8]);
model.component("comp1").physics("tds").feature("fl1").setIndex("species", true, 0);
model.component("comp1").physics("tds").feature("fl1").setIndex("species", true, 1);
model.component("comp1").physics("tds").feature("fl1").setIndex("species", true, 2);
model.component("comp1").physics("tds").feature("fl1").set("IncludeConvection", false);
model.component("comp1").physics("tds").feature("fl1").setIndex("J0", "-(1.55038E-06+5.01467E-04*H)*(1-10^(SI))", 0);
model.component("comp1").physics("tds").feature("fl1").setIndex("J0", "(1.55038E-06+5.01467E-04*H)*(1-10^(SI))", 1);
model.component("comp1").physics("tds").feature("fl1").setIndex("J0", "(1.55038E-06+5.01467E-04*H)*(1-10^(SI))", 2);

model.component('comp1').mesh('mesh1').contribute('physics/spf', true);
model.component('comp1').mesh('mesh1').contribute('physics/tds', true);
model.component('comp1').mesh('mesh1').contribute('common/free1', true);
model.component('comp1').mesh('mesh1').autoMeshSize(3);
model.component('comp1').mesh('mesh1').run;

model.study.create('std1');
model.study('std1').create('time', 'Transient');
model.study('std1').feature('time').activate('spf', true);
model.study('std1').feature('time').activate('tds', true);
model.study('std1').feature('time').activate('free1', true);



model.sol.create('sol1');
model.sol('sol1').study('std1');
model.sol('sol1').attach('std1');
model.sol('sol1').create('st1', 'StudyStep');
model.sol('sol1').create('v1', 'Variables');
model.sol('sol1').create('t1', 'Time');
model.sol('sol1').feature('t1').create('fc1', 'FullyCoupled');
model.sol('sol1').feature('t1').create('d1', 'Direct');
model.sol('sol1').feature('t1').feature.remove('fcDef');

model.study('std1').feature('time').set('tlist', 'range(###)');

model.sol('sol1').attach('std1');
model.sol('sol1').feature('t1').set('tlist', 'range(###)');
model.sol("sol1").feature("t1").set("plot", "off");
model.sol("sol1").feature("t1").set("probesel", "all");
model.sol("sol1").feature("t1").set("probefreq", "tsteps");
model.sol("sol1").feature("t1").set("rtol", 0.005);
model.sol("sol1").feature("t1").set("atolglobalmethod", "scaled");
model.sol("sol1").feature("t1").set("atolglobalfactor", 0.05);
model.sol("sol1").feature("t1").set("atolglobalvaluemethod", "factor");
model.sol("sol1").feature("t1").set("endtimeinterpolation", true);
model.sol("sol1").feature("t1").set("estrat", "exclude");
model.sol("sol1").feature("t1").set("maxorder", 2);
model.sol("sol1").feature("t1").set("stabcntrl", true);
model.sol("sol1").feature("t1").set("bwinitstepfrac", "0.01");
model.sol("sol1").feature("t1").set("control", "time");
model.sol('sol1').runAll;

model.result.export.create('data1', 'Data');
model.result.export.create('data2', 'Data');
model.result.export.create('data3', 'Data');
model.result.export.create('data4', 'Data');
model.result.export.create('data5', 'Data');

model.result.export('data1').set('timeinterp', 'on');
model.result.export('data1').set('unit', {'mol/L' 'mol/L' 'mol/L' 'mol/L' 'mol/L' 'mol/L' 'mol/L' 'mol/L' 'mol/L' 'mol/L' 'mol/L' 'mol/L' 'mol/L' 'mol/L' 'mol/L' 'mol/L'});
model.result.export('data1').set('descr', {'H' 'Ca' 'C' 'Al' 'Na' 'K' 'Fe' 'Mg' 'SO4' 'Si' 'Cl'});
model.result.export('data1').set('expr', {'H' 'Ca' 'C' 'Al' 'Na' 'K' 'Fe' 'Mg' 'SO4' 'Si' 'Cl' 'Fe' 'Mg' 'SO4' 'Si' 'Cl'});
model.result.export('data1').set('t', '0');
model.result.export('data1').set('filename', 'F:\(Comsol+Phreeqc)python\COMSOL_phreeqc\Result\outcon0.txt');

model.result.export('data2').set('timeinterp', 'on');
model.result.export('data2').set('unit', {' ' 'mol/L' 'mol/L' 'mol/L' 'mol/L' 'mol/L' 'mol/L' 'mol/L' 'mol/L' 'mol/L' 'mol/L' 'mol/L' 'mol/L' 'mol/L' 'mol/L' 'mol/L'});
model.result.export('data2').set('descr', {'pH' 'Ca' 'C' 'Al' 'Na' 'K' 'Fe' 'Mg' 'SO4' 'Si' 'Cl'});
model.result.export('data2').set('expr', {'-log10(abs(H/1000))' 'Ca' 'C' 'Al' 'Na' 'K' 'Fe' 'Mg' 'SO4' 'Si' 'Cl' 'Fe' 'Mg' 'SO4' 'Si' 'Cl'});
model.result.export('data2').set('t', '#');
model.result.export('data2').set('filename', 'F:\(Comsol+Phreeqc)python\COMSOL_phreeqc\Result\outcono.txt');

model.result.export('data3').set('descr', {'Pressure'});
model.result.export('data3').set('timeinterp', 'on');
model.result.export('data3').set('filename', 'F:\(Comsol+Phreeqc)python\COMSOL_phreeqc\Result/Pressureo.txt');
model.result.export('data3').set('unit', {'Pa'});
model.result.export('data3').set('t', '#');
model.result.export('data3').set('expr', {'abs(p)'});

model.result.export('data4').set('descr', {'flow velocity'});
model.result.export('data4').set('timeinterp', 'on');
model.result.export('data4').set('filename', 'F:\(Comsol+Phreeqc)python\COMSOL_phreeqc\Result/flowvelocityo.txt');
model.result.export('data4').set('unit', {'m/s' 'm/s'});
model.result.export('data4').set('t', '#');
model.result.export('data4').set('expr', {'u' 'v'});

model.result.export('data5').set('descr', {'material velocity'});
model.result.export('data5').set('timeinterp', 'on');
model.result.export('data5').set('filename', 'F:\(Comsol+Phreeqc)python\COMSOL_phreeqc\Result/materialvelocityo.txt');
model.result.export('data5').set('unit', {'m' 'm'});
model.result.export('data5').set('t', '#');
model.result.export('data5').set('expr', {'material.u' 'material.v'});

model.result.export('data1').run
model.result.export('data2').run
model.result.export('data3').run
model.result.export('data4').run
model.result.export('data5').run

mphmesh(model)
ModelUtil.showProgress(true);
model.save('F:\(Comsol+Phreeqc)python\COMSOL_phreeqc\Result\model_initial')

out = model;

    """
