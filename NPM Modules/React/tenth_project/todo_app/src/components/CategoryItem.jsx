import styled from "styled-components";
import { mobile } from "../responsive";

const Container = styled.div`
  flex: 1;
  margin: 3px;
  height: 70vh;
  position: relative;
  &:hover {
    transform: scale(1.01);
    transition: 0.3s ease-in-out;
  }
  &:not(:hover) {
    transform: scale(1.00);
    transition: 0.5s ease-in-out;
    }
`;

const Image = styled.img`
  width: 100%;
  height: 100%;
  object-fit: cover;
  ${mobile({ height: "20vh" })}
  `;

const Info = styled.div`
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
`;

const Title = styled.h1`
    color:white;
    margin-bottom: 20px;
    background-color: rgba(6, 6, 6, 0.384);
    padding-top: 7px;
    padding-bottom: 7px;
    padding-left: 13px;
    padding-right: 13px;
`;

const Button = styled.button`
    border:none;
    padding: 10px;
    background-color: white;
    color:gray;
    cursor: pointer;
    font-weight: 600;
    &:hover {
    transform: scale(1.2);
    background-color: brown;
    color: #fff;
    transition: 0.3s ease-in-out;
  }
  &:not(:hover) {
    transform: scale(1.00);
    transition: 0.5s ease-in-out;
    }
`;

const CategoryItem = ({ item }) => {
  return (
    <Container>
      <Image src={item.img} />
      <Info>
        <Title>{item.title}</Title>
        <Button>İNCELE</Button>
      </Info>
    </Container>
  );
};

export default CategoryItem;
