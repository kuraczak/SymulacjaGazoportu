im=imread("mapka.png");
rury=[255;255;255];

y=size(im,2)
x=size(im,1)

map=ones(x,y);
for xx=1:x
    for yy=1:y
        rgb=[im(xx,yy,1); im(xx,yy,2); im(xx,yy,3)];
        if  rgb==[0;0;0]             
                map(xx,yy)=0; %droga do inspekcji
        elseif rgb==[0;255;0]
            map(xx,yy)=2; %obszar zagro¿ony
        elseif rgb==[255;0;0]
            map(xx,yy)=3; %zbiornik
         elseif rgb==[255;255;255]
            map(xx,yy)=4; %budynek
         elseif rgb==[0;255;0]
            map(xx,yy)=5; %obszar zagro¿ony
         elseif rgb==[255;255;0]
            map(xx,yy)=6; %obszar ³adowania
         elseif rgb==[0;255;255]
            map(xx,yy)=7; %droga dojazdu do ³adowania
        end
                

    end
end
imshow(map,[]);
csvwrite('matrix.csv',map);