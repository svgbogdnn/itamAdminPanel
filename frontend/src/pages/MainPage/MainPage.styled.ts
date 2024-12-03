import styled from "styled-components";
import { Container as ContentContainer } from "../../components/Content/Content.styled";

export const Wrapper = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 24px;
  height: 100%;

  ${ContentContainer} {
    flex: initial;
  }
`;

export const Container = styled.div`
  display: flex;
  flex-direction: column;
  justify-content: stretch;
  align-items: flex-start;
  gap: 16px;
  width: 100%;
`;

export const Title = styled.h1`
  margin: 0;
  color: #ffffff;
  font-weight: 500;
`;
