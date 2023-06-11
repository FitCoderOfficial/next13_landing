import { MouseEventHandler } from "react";

export interface CustomButtonProps {
    title: string;
    containerStyles?: string;
    handleClick?: 
    MouseEventHandler<HTMLButtonElement> | undefined;
    btnType?: "button" | "submit" | 
}

export interface SearchFoodProps {
    Food: string;
    setFood: (food: string) => void;
}