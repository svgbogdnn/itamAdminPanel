import styled from "styled-components";

export const Container = styled.article`
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  padding: 10px;
  background-color: #323D4E80;
  border: 1px solid #000000;
  border-radius: 24px;
  box-shadow: 0 0 8px 0 #00000040;
`;

export const Header = styled.div`
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  padding: 20px;
`;

export const Group = styled.div`
  display: flex;
  justify-content: flex-start;
  align-items: center;
  gap: 12px;
`;

export const Field = styled.div`
  color: #ffffff;
  font-family: Actay Wide;
  font-weight: 700;
  font-size: 14px;
  line-height: 1.42;
`;

export const Comment = styled.p`
  padding: 10px 20px;
  margin: 0;
  color: #FFFFFFE5;
  font-family: Actay;
  font-size: 14px;
  font-weight: 400;
  line-height: 1.42;
`;

export const Footer = styled(Header)`
  padding: 10px 20px;
`;
