filename='/home/ozan/Desktop/lol/15_dehaze';
reducehaze(filename);
lo=imread(filename);
% figure;
% imshow(lo);
imwrite(lo,'/home/ozan/Desktop/lol/01','jpg');
% File                 = 'C:/Your/Folder/Na.me.txt';
% [fPath, fName, fExt] = fileparts(File);
% strcat(fPath,fName)