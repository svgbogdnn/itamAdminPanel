import styled from "styled-components";

export const Container = styled.div`
  display: flex;
  justify-content: flex-start;
  align-items: flex-start;
  gap: 9px;
  margin-left: 19px;
`;

export const Avatar = styled.img`
  width: 30px;
  height: 30px;
  border-radius: 50%;
  overflow: hidden;
  object-fit: cover;
`;

export const Content = styled.div`
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  gap: 3px;
`;

export const Name = styled.span`
  font-family: Nunito Sans;
  font-weight: 700;
  font-size: 12px;
  line-height: 1.36;
`;

export const Role = styled.span`
  font-family: Nunito Sans;
  font-weight: 600;
  font-size: 10px;
  line-height: 1.36;
`;
