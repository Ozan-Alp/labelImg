function reducehaze(filename) %#codegen
A = imread(filename);
info = imfinfo(filename);
if isfield(info, 'Orientation')
    %fprintf("Orientation found");
if info.Orientation == 8
    A=imrotate(A,90);
elseif info.Orientation ==6
    A=imrotate(A,-90);
elseif info.Orientation ==3
    A=imrotate(A,180);
elseif info.Orientation ==2
    A=flip(A,2);
elseif info.Orientation ==5
    A=imrotate(A,-90);
    A=flip(A,2);
elseif info.Orientation ==7
    A=imrotate(A,90);
    A=flip(A,2);
elseif info.Orientation ==4
    A=imrotate(A,180);
    A=flip(A,2);
end
end
AInv = imcomplement(A);
BInv = imreducehaze(AInv, 'Method','approx','ContrastEnhancement','boost');
BImp = imcomplement(BInv);
% split_path=split(filename, '.')
% path=string(split_path(1))
[fPath, fName, ~] = fileparts(filename);
path=fullfile(fPath,fName);
file_name = strcat(path,'_dehaze.jpg');%os otomatik extensionu extensiona yaziyor filename yazmiyor
imwrite(BImp, file_name, 'jpg');
%fprintf("matlab image written.");
end

%figure, montage({A,B,BImp});
%A = imread("/home/ozan/Downloads/111haze.jpg");
% info = imfinfo("/home/ozan/Desktop/lol/01genshin.jpg");
% if isfield(info, 'Orientation')
%     fprintf('lol')
% else
%     fprintf('kok\n')
% end
%% matlab versiyonu
% function reducehaze(varargin) %#codegen
% A = imread(varargin{1});
% info = imfinfo(varargin{1});
% if info.Orientation ==8
%     A=imrotate(A,90);
% elseif info.Orientation ==6
%     A=imrotate(A,-90);
% elseif info.Orientation ==3
%     A=imrotate(A,180);
% elseif info.Orientation ==2
%     A=flip(A,2);
% elseif info.Orientation ==5
%     A=imrotate(A,-90);
%     A=flip(A,2);
% elseif info.Orientation ==7
%     A=imrotate(A,90);
%     A=flip(A,2);
% elseif info.Orientation ==4
%     A=imrotate(A,180);
%     A=flip(A,2);
% end
% 
% AInv = imcomplement(A);
% BInv = imreducehaze(AInv, 'Method','approx','ContrastEnhancement','boost');
% BImp = imcomplement(BInv);
% split_path=split(varargin{1}, '.')
% path=string(split_path(1))
% file_name = strcat(path,'_dehaze.jpg')
% imwrite(BImp, file_name);
% end

%%

%%%%% deneme%%%%
% tic;
% A = imread('/home/ozan/Desktop/resler/train/18.jpg');
% info = imfinfo('/home/ozan/Desktop/resler/train/18.jpg');
% if info.Orientation ==8
%     A=imrotate(A,90);
% elseif info.Orientation ==6
%     A=imrotate(A,-90);
% elseif info.Orientation ==3
%     A=imrotate(A,180);
% elseif info.Orientation ==2
%     A=flip(A,2);
% elseif info.Orientation ==5
%     A=imrotate(A,-90);
%     A=flip(A,2);
% elseif info.Orientation ==7
%     A=imrotate(A,90);
%     A=flip(A,2);
% elseif info.Orientation ==4
%     A=imrotate(A,180);
%     A=flip(A,2);
% end
% AInv = imcomplement(A);
% BInv = imreducehaze(AInv, 'Method','approx','ContrastEnhancement','boost');
% BImp = imcomplement(BInv);
% split_path=split('/home/ozan/Desktop/resler/train/18.jpg', '.')
% path=split_path(1)
% file_name = strcat('/home/ozan/Desktop/resler/train/18','_dehaze.jpg')
% imwrite(BImp, file_name);
% figure, montage({A,BInv,BImp});
% toc
