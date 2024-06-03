{ pkgs ? import <nixpkgs> {} }: with pkgs; mkShell { buildInputs = [
python312Packages.tkinter
python312Packages.pygame
];shellHook="export LD_LIBRARY_PATH=${stdenv.cc.cc.lib}/lib/:$LD_LIBRARY_PATH";}

